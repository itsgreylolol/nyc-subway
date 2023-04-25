using System;
using Microsoft.EntityFrameworkCore.Migrations;
using MySql.EntityFrameworkCore.Metadata;

#nullable disable

namespace backend.Migrations
{
    /// <inheritdoc />
    public partial class InitStops : Migration
    {
        /// <inheritdoc />
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropTable(name: "Stops");

            migrationBuilder.AlterDatabase().Annotation("MySQL:Charset", "utf8mb4");

            migrationBuilder
                .CreateTable(
                    name: "Stops",
                    columns: table =>
                        new
                        {
                            Id = table.Column<Guid>(type: "char(36)", nullable: false),
                            Name = table.Column<string>(type: "longtext", nullable: true),
                            Latitude = table.Column<float>(type: "float", nullable: false),
                            Longitude = table.Column<float>(type: "float", nullable: false),
                            LastUpdated = table
                                .Column<DateTime>(type: "datetime(6)", nullable: false)
                                .Annotation(
                                    "MySQL:ValueGenerationStrategy",
                                    MySQLValueGenerationStrategy.ComputedColumn
                                ),
                            Created = table
                                .Column<DateTime>(type: "datetime(6)", nullable: false)
                                .Annotation(
                                    "MySQL:ValueGenerationStrategy",
                                    MySQLValueGenerationStrategy.IdentityColumn
                                )
                        },
                    constraints: table =>
                    {
                        table.PrimaryKey("PK_Stops", x => x.Id);
                    }
                )
                .Annotation("MySQL:Charset", "utf8mb4");
        }

        /// <inheritdoc />
        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropTable(name: "Stops");
        }
    }
}
