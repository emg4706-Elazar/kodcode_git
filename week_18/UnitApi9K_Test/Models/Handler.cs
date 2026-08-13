using System.ComponentModel.DataAnnotations;
using Microsoft.EntityFrameworkCore;

namespace UnitApi9K.Models;

[Index(nameof(PersonalNumber), IsUnique = true)]
public class Handler
{
    public int Id { get; set; }
    public Dog? Dog { get; set; }

    [Required]
    [MaxLength(100)]
    public string FullName { get; set; } = string.Empty;

    [Required]
    [MaxLength(10)]
    public string PersonalNumber { get; set; } = string.Empty;

    [Required]
    [MaxLength(30)]
    public string Rank { get; set; } = string.Empty;

    [Required]
    [Range(0, 40)]
    public int YearsOfExperience { get; set; }

    [Required]
    [MaxLength(100)]
    public string BaseAssigned { get; set; } = string.Empty;
}
