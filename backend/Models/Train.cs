public class Train : BaseModel
{
    public string Type { get; set; }

    public List<Car> Cars { get; set; }

    public int MaxCapacity => Cars.Select(c => c.MaxCapacity).Sum();

    public Train()
    {
        Type = string.Empty;
        Cars = new List<Car>();
    }
}
