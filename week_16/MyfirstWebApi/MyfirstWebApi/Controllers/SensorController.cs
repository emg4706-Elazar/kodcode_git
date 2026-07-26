using MyfirstWebApi;
using Microsoft.AspNetCore.Mvc;
using System.Collections;

namespace MyfirstWebApi.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class SensorController :ControllerBase
    {
        private static readonly List<Site> _sites = new()
        {
            new Site { Id = 1, Name = "Alpha Station", Zone = "North", Status = "Active" },
            new Site { Id = 2, Name = "Beta Outpost", Zone = "South", Status = "Maintenance" },
            new Site { Id = 3, Name = "Gamma Hub", Zone = "East", Status = "Active" },
            new Site { Id = 4, Name = "Delta Unit", Zone = "West", Status = "Offline" },
            new Site { Id = 5, Name = "Epsilon Facility", Zone = "North", Status = "Active" },
            new Site { Id = 6, Name = "Zeta Relay", Zone = "South", Status = "Error" },
            new Site { Id = 7, Name = "Eta Station", Zone = "East", Status = "Maintenance" },
            new Site { Id = 8, Name = "Theta Terminal", Zone = "West", Status = "Active" }
        };

        [HttpGet]
        public ActionResult<IEnumerable<Site>> GetAllSites()
        {
            return Ok(_sites);
        }

        [HttpGet("{id}")]
        public ActionResult<Site> GetSiteById(int id)
        {
            var site = _sites.FirstOrDefault(s => s.Id == id);

            if (site == null)
            {
                return NotFound();
            }

            return Ok(site);
        }

        [HttpGet("filterByZone")]
        public ActionResult<IEnumerable<Site>> FilterByZone(
            [FromQuery] string? zone)
        {
            var filterdSites = _sites.Where(s => s.Zone.ToLower() == zone);

            if (!filterdSites.Any())
            {
                return NotFound();
            }

            return Ok(filterdSites);
        }
    }
}
