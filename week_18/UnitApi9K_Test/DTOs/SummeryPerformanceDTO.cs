using UnitApi9K.Enums;

namespace UnitApi9K.DTOs;

public class SummeryPerformanceDTO
{
    public int DogId { get; set; }
    public string DogName { get; set; } = string.Empty;
    public SpecialtyTypes Specialty { get; set; }
    public int TrainingsCount { get; set; }
    public double AveragePerformance { get; set; }
}
