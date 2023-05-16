using System.Text.Json.Serialization;

// https://stackoverflow.com/a/27883916
public class Coordinate
{
    [JsonIgnore]
    private const double _radiusEarthMiles = 3959;

    [JsonIgnore]
    private const double _m2km = 1.60934;

    [JsonIgnore]
    private const double _toRad = Math.PI / 180;

    public double Latitude { get; set; }

    public double Longitude { get; set; }

    public double GetHaversineDistance(Coordinate dest, bool km = false)
    {
        double _radLat1 = this.Latitude * _toRad;
        double _radLat2 = dest.Latitude * _toRad;
        double _dLatHalf = (_radLat2 - _radLat1) / 2;
        double _dLonHalf = Math.PI * (dest.Longitude - this.Longitude) / 360;

        // intermediate result
        double _a = Math.Sin(_dLatHalf);
        _a *= _a;

        // intermediate result
        double _b = Math.Sin(_dLonHalf);
        _b *= _b * Math.Cos(_radLat1) * Math.Cos(_radLat2);

        // central angle, aka arc segment angular distance
        double _centralAngle = 2 * Math.Atan2(Math.Sqrt(_a + _b), Math.Sqrt(1 - _a - _b));

        // great-circle (orthodromic) distance on Earth between 2 points
        double distanceInMiles = _radiusEarthMiles * _centralAngle;

        if (km)
            return distanceInMiles * _m2km;

        return distanceInMiles;
    }

    public double GetSEPDistance(Coordinate dest, bool km = false)
    {
        double _radLat1 = this.Latitude * _toRad;
        double _radLat2 = dest.Latitude * _toRad;
        double _dLat = (_radLat2 - _radLat1);
        double _dLon = (dest.Longitude - this.Longitude) * _toRad;

        double _a = (_dLon) * Math.Cos((_radLat1 + _radLat2) / 2);

        // central angle, aka arc segment angular distance
        double _centralAngle = Math.Sqrt(_a * _a + _dLat * _dLat);

        // great-circle (orthodromic) distance on Earth between 2 points
        double distanceInMiles = _radiusEarthMiles * _centralAngle;

        if (km)
            return distanceInMiles * _m2km;

        return distanceInMiles;
    }
}
