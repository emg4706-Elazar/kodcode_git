using Microsoft.EntityFrameworkCore.Migrations;

#nullable disable

namespace UnitApi9K.Migrations
{
    /// <inheritdoc />
    public partial class fixdbdelete : Migration
    {
        /// <inheritdoc />
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropForeignKey(
                name: "FK_Dogs_Handlers_HandlerId",
                table: "Dogs");

            migrationBuilder.AddForeignKey(
                name: "FK_Dogs_Handlers_HandlerId",
                table: "Dogs",
                column: "HandlerId",
                principalTable: "Handlers",
                principalColumn: "Id",
                onDelete: ReferentialAction.SetNull);
        }

        /// <inheritdoc />
        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropForeignKey(
                name: "FK_Dogs_Handlers_HandlerId",
                table: "Dogs");

            migrationBuilder.AddForeignKey(
                name: "FK_Dogs_Handlers_HandlerId",
                table: "Dogs",
                column: "HandlerId",
                principalTable: "Handlers",
                principalColumn: "Id");
        }
    }
}
