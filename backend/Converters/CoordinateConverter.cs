using System.Text.Json;
using Microsoft.EntityFrameworkCore.Storage.ValueConversion;

public class CoordinateConverter : ValueConverter<Coordinate?, string>
{
    public CoordinateConverter()
        : base(
            v => JsonSerializer.Serialize(v, new JsonSerializerOptions()),
            v => JsonSerializer.Deserialize<Coordinate>(v, new JsonSerializerOptions())
        ) { }
}
