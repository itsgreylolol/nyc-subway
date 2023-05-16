public class Car : BaseModel
{
    public string Type { get; set; }

    public int MaxCapacity { get; set; }

    public Train? Train { get; set; }

    public Car()
    {
        Type = string.Empty;
    }
}
