using UnitApi9K.Enums;

namespace UnitApi9K.DTOs;

public class DogWithHanlerDTO
{
    public int DogId { get; set; }
    public string DogName { get; set; } = string.Empty;
    public string Breed { get; set; } = string.Empty;
    public SpecialtyTypes Specialty { get; set; }
    public StatusTypes Status { get; set; }
    public string? HandlerName { get; set; } = string.Empty;
    public string? HandlerRank { get; set; } = string.Empty;
}
