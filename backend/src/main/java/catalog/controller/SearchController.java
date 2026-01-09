package catalog.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import java.util.Map;
import java.util.List;
import org.springframework.web.bind.annotation.RequestParam;

@RestController
public class SearchController {

	@GetMapping("/api/search")
	public Map<String, Object> search(
			@RequestParam(defaultValue = "") String q) {
		return Map.of(
				"query", q,
				"results", List.of(),
				"total", 0);
	}

}
