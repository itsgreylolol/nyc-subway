class Program
{
    static void Main(string[] args)
    {
        InitDatabase();
        var builder = WebApplication.CreateBuilder(args);
        var app = builder.Build();

        app.Run();
    }

    private static void InitDatabase()
    {
        using var context = new NYCSubwayContext();
        context.Database.EnsureCreated();
    }
}
