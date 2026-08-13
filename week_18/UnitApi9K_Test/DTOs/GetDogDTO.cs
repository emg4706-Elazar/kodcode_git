using UnitApi9K.Enums;

namespace UnitApi9K.DTOs;

public class GetDogDTO
{
    public int Id { get; set; }
    public string Name { get; set; } = string.Empty;
    public string Breed { get; set; } = string.Empty;
    public string MicrochipId { get; set; } = string.Empty;
    public DateTime DateOfBirth { get; set; }
    public SpecialtyTypes Specialty { get; set; }
    public StatusTypes Status { get; set; }
}
