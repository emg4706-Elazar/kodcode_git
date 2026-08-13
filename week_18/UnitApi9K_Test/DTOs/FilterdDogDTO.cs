using UnitApi9K.Enums;

namespace UnitApi9K.DTOs;

public class FilterdDogDTO
{
    public int Id { get; set; }
    public string Name { get; set; } = string.Empty;
    public string Breed { get; set; } = string.Empty;
    public SpecialtyTypes Specialty { get; set; }
    public StatusTypes Status { get; set; }
}
