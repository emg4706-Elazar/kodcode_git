using Microsoft.EntityFrameworkCore;
using UnitApi9K.Models;
using UnitApi9K.Enums;

namespace UnitApi9K.Data;


// Define the tables
public class AppDbContext : DbContext
{
    public AppDbContext(
        DbContextOptions<AppDbContext> options)
        : base(options)
    {
    }

    public DbSet<Handler> Handlers => Set<Handler>();
    public DbSet<Dog> Dogs => Set<Dog>();
    public DbSet<TrainingSession> TrainingSessions => Set<TrainingSession>();


    // Define the Relationships
    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        base.OnModelCreating(modelBuilder);

        // Define the enums as string
        modelBuilder.Entity<Dog>()
            .Property(d => d.Specialty) // SpecialtyTypes
            .HasConversion<string>();

        modelBuilder.Entity<Dog>()
            .Property(d => d.Status) // Statustypes
            .HasConversion<string>();

        modelBuilder.Entity<TrainingSession>()
            .Property(t => t.TrainingType) // TrainingTypes
            .HasConversion<string>();


        // Define the relationships
        modelBuilder.Entity<Dog>()
            .HasOne(d => d.Handler)
            .WithOne(h => h.Dog)
            .HasForeignKey<Dog>(d => d.HandlerId)
            .OnDelete(DeleteBehavior.SetNull);

        modelBuilder.Entity<TrainingSession>()
            .HasOne(t => t.Dog)
            .WithMany(d => d.Trainings)
            .HasForeignKey(t => t.DogId)
            .OnDelete(DeleteBehavior.Cascade);
    }
}
