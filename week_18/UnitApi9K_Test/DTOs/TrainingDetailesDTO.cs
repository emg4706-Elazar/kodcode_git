using System.ComponentModel.DataAnnotations;
using UnitApi9K.Enums;
using UnitApi9K.Models;

namespace UnitApi9K.DTOs;

public class TrainingDetailesDTO
{
    public int Id { get; set; }
    public int DogId { get; set; }
    public string DogName { get; set; } = string.Empty;
    public SpecialtyTypes Specialty { get; set; }
    public DateTime SessionDate { get; set; }
    public int DurationMinutes { get; set; }
    public TrainingTypes TrainingType { get; set; }
    public int PerformanceScore { get; set; }
    public bool Passed { get; set; }
    public string Evaluator { get; set; } = string.Empty;
    public string? HandlerName { get; set; } = string.Empty;

}
