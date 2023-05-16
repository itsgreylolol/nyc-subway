public class Stop : BaseModel
{
    public string Name { get; set; }

    public Coordinate Coordinate { get; set; }

    public Train? Train { get; set; }

    public Stop()
    {
        Name = string.Empty;
        Coordinate = new Coordinate();
    }
}
