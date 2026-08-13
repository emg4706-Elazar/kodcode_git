using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
using Microsoft.EntityFrameworkCore;
using UnitApi9K.Enums;

namespace UnitApi9K.Models;

[Index(nameof(MicrochipId), IsUnique = true)]
public class Dog
{
    public int Id { get; set; }
    public int? HandlerId { get; set; }
    public Handler? Handler { get; set; }

    [Required]
    [MaxLength(50)]
    public string Name { get; set; } = string.Empty;

    [Required]
    [MaxLength(50)]
    public string Breed { get; set; } = string.Empty;

    [Required]
    [MaxLength(15)]
    public string MicrochipId { get; set; } = string.Empty;

    [Required]
    public DateTime DateOfBirth { get; set; }

    [Required]
    public SpecialtyTypes Specialty { get; set; }

    [Required]
    public StatusTypes Status { get; set; }

    public ICollection<TrainingSession> Trainings { get; set; } = new List<TrainingSession>();
}
