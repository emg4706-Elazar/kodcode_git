using Microsoft.EntityFrameworkCore.Migrations;

#nullable disable

namespace UnitApi9K.Migrations
{
    /// <inheritdoc />
    public partial class FixedNames : Migration
    {
        /// <inheritdoc />
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropForeignKey(
                name: "FK_Trainings_Dogs_DogId",
                table: "Trainings");

            migrationBuilder.DropPrimaryKey(
                name: "PK_Trainings",
                table: "Trainings");

            migrationBuilder.RenameTable(
                name: "Trainings",
                newName: "TrainingSessions");

            migrationBuilder.RenameIndex(
                name: "IX_Trainings_DogId",
                table: "TrainingSessions",
                newName: "IX_TrainingSessions_DogId");

            migrationBuilder.AddPrimaryKey(
                name: "PK_TrainingSessions",
                table: "TrainingSessions",
                column: "Id");

            migrationBuilder.AddForeignKey(
                name: "FK_TrainingSessions_Dogs_DogId",
                table: "TrainingSessions",
                column: "DogId",
                principalTable: "Dogs",
                principalColumn: "Id",
                onDelete: ReferentialAction.Cascade);
        }

        /// <inheritdoc />
        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropForeignKey(
                name: "FK_TrainingSessions_Dogs_DogId",
                table: "TrainingSessions");

            migrationBuilder.DropPrimaryKey(
                name: "PK_TrainingSessions",
                table: "TrainingSessions");

            migrationBuilder.RenameTable(
                name: "TrainingSessions",
                newName: "Trainings");

            migrationBuilder.RenameIndex(
                name: "IX_TrainingSessions_DogId",
                table: "Trainings",
                newName: "IX_Trainings_DogId");

            migrationBuilder.AddPrimaryKey(
                name: "PK_Trainings",
                table: "Trainings",
                column: "Id");

            migrationBuilder.AddForeignKey(
                name: "FK_Trainings_Dogs_DogId",
                table: "Trainings",
                column: "DogId",
                principalTable: "Dogs",
                principalColumn: "Id",
                onDelete: ReferentialAction.Cascade);
        }
    }
}
