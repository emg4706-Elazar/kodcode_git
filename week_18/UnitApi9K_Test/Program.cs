using UnitApi9K.Data;
using Microsoft.EntityFrameworkCore;
using UnitApi9K.Repositories;

var builder = WebApplication.CreateBuilder(args);

// Add services to the container.
builder.Services.AddControllers();
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

// Get the connection string
var connectionString = builder.Configuration
    .GetConnectionString("DefaultConnection");

// Register the AppDbContext
builder.Services.AddDbContext<AppDbContext>(options =>
options.UseMySql(connectionString,
ServerVersion.AutoDetect(connectionString))
);

// Register the repositories
builder.Services.AddScoped<IUnitRepository, UnitRepository>();

var app = builder.Build();

// Configure the HTTP request pipeline.
if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

app.UseHttpsRedirection();

app.UseAuthorization();

app.MapControllers();

app.Run();
