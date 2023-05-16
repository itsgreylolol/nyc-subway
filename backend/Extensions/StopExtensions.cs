public static class StopExtensions
{
    public static double GetHaversineDistance(this Stop source, Stop dest, bool km = false) =>
        source.Coordinate.GetHaversineDistance(dest.Coordinate, km);

    public static double GetSEPDistance(this Stop source, Stop dest, bool km = false) =>
        source.Coordinate.GetSEPDistance(dest.Coordinate, km);
}
