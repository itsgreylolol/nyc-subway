using Microsoft.EntityFrameworkCore;

public class NYCSubwayContext : DbContext
{
    public DbSet<Stop> Stops { get; set; }

    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        base.OnModelCreating(modelBuilder);
    }

    protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
    {
        IConfigurationRoot configuration = new ConfigurationBuilder()
            .SetBasePath(AppDomain.CurrentDomain.BaseDirectory)
            .AddJsonFile("appsettings.json")
            .Build();
        optionsBuilder.UseMySQL(configuration.GetConnectionString("NYCSubwayContext"));
    }
}
