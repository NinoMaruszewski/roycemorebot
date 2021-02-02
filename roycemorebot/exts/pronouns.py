import asyncio
import logging

import discord
from discord.ext import commands

from roycemorebot.checks import has_any_role_check
from roycemorebot.constants import Channels, PronounRoles

log = logging.getLogger(__name__)

PRONOUN_ROLES = [PronounRoles.he_him, PronounRoles.she_her, PronounRoles.they_them]


class Pronouns(commands.Cog, name="Pronoun Roles"):
    """User-assigned roles based on their grade."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.guild_only()
    @commands.command(name="he-him", aliases=("he", "him", "hehim"))
    async def he_him(self, ctx: commands.Context) -> None:
        """Self-give the `He/Him` Role."""
        # User is switching roles, remove all current roles
        if await has_any_role_check(ctx, *PRONOUN_ROLES):
            for role in PRONOUN_ROLES:
                await ctx.author.remove_roles(
                    discord.Object(role),
                    reason=f"{ctx.author} changing pronoun roles",
                )

        await ctx.author.add_roles(
            discord.Object(PronounRoles.he_him), reason="Pronoun Roles"
        )
        log.info(f"Assigned {ctx.author} the He/Him role")

        if ctx.message.channel.id == Channels.roles:
            await ctx.send(
                f"{ctx.author.mention}, you have successfully been given the He/Him "
                + "role.",
                delete_after=5.0,
            )
            await asyncio.sleep(5.0)
            await ctx.message.delete()
        else:
            await ctx.send(
                f"{ctx.author.mention}, you have successfully been given the He/Him "
                + "role.",
            )

    @commands.guild_only()
    @commands.command(name="she-her", aliases=("she", "her", "sheher"))
    async def she_her(self, ctx: commands.Context) -> None:
        """Self-give the `She/Her` Role."""
        # User is switching roles, remove all current roles
        if await has_any_role_check(ctx, *PRONOUN_ROLES):
            for role in PRONOUN_ROLES:
                await ctx.author.remove_roles(
                    discord.Object(role),
                    reason=f"{ctx.author} changing pronoun roles",
                )

        await ctx.author.add_roles(
            discord.Object(PronounRoles.she_her), reason="Pronoun Roles"
        )
        log.info(f"Assigned {ctx.author} the She/Her role")

        if ctx.message.channel.id == Channels.roles:
            await ctx.send(
                f"{ctx.author.mention}, you have successfully been given the She/Her "
                + "role.",
                delete_after=5.0,
            )
            await asyncio.sleep(5.0)
            await ctx.message.delete()
        else:
            await ctx.send(
                f"{ctx.author.mention}, you have successfully been given the She/Her "
                + "role.",
            )

    @commands.guild_only()
    @commands.command(name="they-them", aliases=("they", "them", "theythem"))
    async def they_them(self, ctx: commands.Context) -> None:
        """Self-give the `They/Them` Role."""
        # User is switching roles, remove all current roles
        if await has_any_role_check(ctx, *PRONOUN_ROLES):
            for role in PRONOUN_ROLES:
                await ctx.author.remove_roles(
                    discord.Object(role),
                    reason=f"{ctx.author} changing pronoun roles",
                )

        await ctx.author.add_roles(
            discord.Object(PronounRoles.they_them), reason="Pronoun Roles"
        )
        log.info(f"Assigned {ctx.author} the They/Them role")

        if ctx.message.channel.id == Channels.roles:
            await ctx.send(
                f"{ctx.author.mention}, you have successfully been given the They/Them "
                + "role.",
                delete_after=5.0,
            )
            await asyncio.sleep(5.0)
            await ctx.message.delete()
        else:
            await ctx.send(
                f"{ctx.author.mention}, you have successfully been given the They/Them "
                + "role.",
            )


def setup(bot: commands.Bot) -> None:
    """Add the Pronouns cog to the bot."""
    bot.add_cog(Pronouns(bot))
