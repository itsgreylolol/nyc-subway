using Microsoft.EntityFrameworkCore;

public class NYCSubwayContext : DbContext
{
    public DbSet<Stop> Stops => Set<Stop>();

    public DbSet<Car> Cars => Set<Car>();

    public DbSet<Train> Trains => Set<Train>();

    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        base.OnModelCreating(modelBuilder);
    }

    protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
    {
        IConfigurationRoot configuration = new ConfigurationBuilder()
            .SetBasePath(AppDomain.CurrentDomain.BaseDirectory)
            .AddJsonFile("appsettings.Development.json")
            .Build();
        optionsBuilder.UseMySQL(configuration.GetConnectionString("NYCSubwayContext") ?? "");
    }

    protected override void ConfigureConventions(ModelConfigurationBuilder configurationBuilder)
    {
        configurationBuilder.Properties<Coordinate>().HaveConversion<CoordinateConverter>();
    }
}
