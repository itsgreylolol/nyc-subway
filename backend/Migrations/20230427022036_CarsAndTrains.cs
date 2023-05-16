using System;
using Microsoft.EntityFrameworkCore.Migrations;
using MySql.EntityFrameworkCore.Metadata;

#nullable disable

namespace backend.Migrations
{
    /// <inheritdoc />
    public partial class CarsAndTrains : Migration
    {
        /// <inheritdoc />
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropColumn(
                name: "Latitude",
                table: "Stops");

            migrationBuilder.DropColumn(
                name: "Longitude",
                table: "Stops");

            migrationBuilder.AlterColumn<string>(
                name: "Name",
                table: "Stops",
                type: "longtext",
                nullable: false,
                defaultValue: "",
                oldClrType: typeof(string),
                oldType: "longtext",
                oldNullable: true);

            migrationBuilder.AddColumn<string>(
                name: "Coordinate",
                table: "Stops",
                type: "longtext",
                nullable: false);

            migrationBuilder.AddColumn<Guid>(
                name: "TrainId",
                table: "Stops",
                type: "char(36)",
                nullable: true);

            migrationBuilder.CreateTable(
                name: "Trains",
                columns: table => new
                {
                    Id = table.Column<Guid>(type: "char(36)", nullable: false),
                    Type = table.Column<string>(type: "longtext", nullable: false),
                    LastUpdated = table.Column<DateTime>(type: "datetime(6)", nullable: false)
                        .Annotation("MySQL:ValueGenerationStrategy", MySQLValueGenerationStrategy.ComputedColumn),
                    Created = table.Column<DateTime>(type: "datetime(6)", nullable: false)
                        .Annotation("MySQL:ValueGenerationStrategy", MySQLValueGenerationStrategy.IdentityColumn)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_Trains", x => x.Id);
                })
                .Annotation("MySQL:Charset", "utf8mb4");

            migrationBuilder.CreateTable(
                name: "Cars",
                columns: table => new
                {
                    Id = table.Column<Guid>(type: "char(36)", nullable: false),
                    Type = table.Column<string>(type: "longtext", nullable: false),
                    MaxCapacity = table.Column<int>(type: "int", nullable: false),
                    TrainId = table.Column<Guid>(type: "char(36)", nullable: true),
                    LastUpdated = table.Column<DateTime>(type: "datetime(6)", nullable: false)
                        .Annotation("MySQL:ValueGenerationStrategy", MySQLValueGenerationStrategy.ComputedColumn),
                    Created = table.Column<DateTime>(type: "datetime(6)", nullable: false)
                        .Annotation("MySQL:ValueGenerationStrategy", MySQLValueGenerationStrategy.IdentityColumn)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_Cars", x => x.Id);
                    table.ForeignKey(
                        name: "FK_Cars_Trains_TrainId",
                        column: x => x.TrainId,
                        principalTable: "Trains",
                        principalColumn: "Id");
                })
                .Annotation("MySQL:Charset", "utf8mb4");

            migrationBuilder.CreateIndex(
                name: "IX_Stops_TrainId",
                table: "Stops",
                column: "TrainId");

            migrationBuilder.CreateIndex(
                name: "IX_Cars_TrainId",
                table: "Cars",
                column: "TrainId");

            migrationBuilder.AddForeignKey(
                name: "FK_Stops_Trains_TrainId",
                table: "Stops",
                column: "TrainId",
                principalTable: "Trains",
                principalColumn: "Id");
        }

        /// <inheritdoc />
        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropForeignKey(
                name: "FK_Stops_Trains_TrainId",
                table: "Stops");

            migrationBuilder.DropTable(
                name: "Cars");

            migrationBuilder.DropTable(
                name: "Trains");

            migrationBuilder.DropIndex(
                name: "IX_Stops_TrainId",
                table: "Stops");

            migrationBuilder.DropColumn(
                name: "Coordinate",
                table: "Stops");

            migrationBuilder.DropColumn(
                name: "TrainId",
                table: "Stops");

            migrationBuilder.AlterColumn<string>(
                name: "Name",
                table: "Stops",
                type: "longtext",
                nullable: true,
                oldClrType: typeof(string),
                oldType: "longtext");

            migrationBuilder.AddColumn<float>(
                name: "Latitude",
                table: "Stops",
                type: "float",
                nullable: false,
                defaultValue: 0f);

            migrationBuilder.AddColumn<float>(
                name: "Longitude",
                table: "Stops",
                type: "float",
                nullable: false,
                defaultValue: 0f);
        }
    }
}
