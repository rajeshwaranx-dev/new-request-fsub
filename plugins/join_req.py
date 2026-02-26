import logging
from pyrogram import Client, filters
from pyrogram.types import ChatJoinRequest
from pyrogram.errors import PeerIdInvalid, ChatAdminRequired, ChannelPrivate
from database.users_chats_db import db
from info import ADMINS, AUTH_CHANNEL

logger = logging.getLogger(__name__)

# ─────────────────────────────────────────────────────────────────────────────
# IMPORTANT SETUP NOTE FOR PRIVATE GROUPS / REQUEST-TO-JOIN MODE
# ─────────────────────────────────────────────────────────────────────────────
# 1. AUTH_CHANNEL must be the numeric chat ID (e.g. -1001234567890).
#    Private groups do NOT have public usernames, so a @username will NOT work.
#
# 2. The bot must be an ADMIN in the group/channel to:
#    a) Receive join request events (chat_join_request)
#    b) Call get_chat_member() to verify membership
#
# 3. For "Request to Join" groups:
#    - Enable "Approve New Members" in the group settings.
#    - The bot will record every incoming request in the DB.
#    - Users with a recorded request are treated as subscribed immediately,
#      so they aren't blocked while waiting for admin approval.
#    - Use /delreq (admin command) to clear the request records when needed.
# ─────────────────────────────────────────────────────────────────────────────


def _build_chat_filter():
    """
    Build a pyrogram chat filter for AUTH_CHANNEL.

    Handles both a single value (int or str) and a list/tuple of values,
    so the handler fires for any configured FSub channel or group.
    """
    if isinstance(AUTH_CHANNEL, (list, tuple)):
        return filters.chat(AUTH_CHANNEL)
    return filters.chat(AUTH_CHANNEL)


@Client.on_chat_join_request(_build_chat_filter())
async def join_reqs(client: Client, request: ChatJoinRequest):
    """
    Triggered when a user sends a 'Request to Join' in the FSub group/channel.

    Stores the user's ID in the database so is_req_subscribed() can recognise
    them as having requested access, even before an admin approves the request.

    Works for:
      - Public channels with join requests enabled
      - Private channels with join requests enabled
      - Private groups with "Approve New Members" enabled
    """
    user_id = request.from_user.id

    try:
        # Only insert once — find_join_req returns True if already stored
        if not await db.find_join_req(user_id):
            await db.add_join_req(user_id)
            logger.info("FSub: Recorded join request from user %s in chat %s", user_id, request.chat.id)
    except Exception as e:
        logger.exception("FSub: Failed to store join request for user %s: %s", user_id, e)


@Client.on_message(filters.command("delreq") & filters.private & filters.user(ADMINS))
async def del_requests(client: Client, message):
    """
    Admin command to clear ALL stored join-request records.

    Use this after pruning users from the FSub group so their old DB records
    don't let them bypass the subscription check.
    """
    try:
        await db.del_join_req()
        await message.reply("<b>⚙ ꜱᴜᴄᴄᴇꜱꜱғᴜʟʟʏ ᴄʜᴀɴɴᴇʟ ʟᴇғᴛ ᴜꜱᴇʀꜱ ᴅᴇʟᴇᴛᴇᴅ</b>")
        logger.info("FSub: All join request records cleared by admin %s", message.from_user.id)
    except Exception as e:
        logger.exception("FSub: Failed to clear join request records: %s", e)
        await message.reply("<b>❌ ᴇʀʀᴏʀ ᴡʜɪʟᴇ ᴄʟᴇᴀʀɪɴɢ ʀᴇᴄᴏʀᴅꜱ. ᴄʜᴇᴄᴋ ʟᴏɢꜱ.</b>")
      
