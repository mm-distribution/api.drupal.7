# DrupalSetContentTestCase::testRegions()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 1410–1437 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L1410-L1437)
- **Class:** [DrupalSetContentTestCase](../DrupalSetContentTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testRegions()
```

## Documentation

```text
Test setting and retrieving content for theme regions.
```

## Code

```php
  function testRegions() {
    global $theme_key;

    $block_regions = system_region_list($theme_key, REGIONS_ALL, FALSE);
    $delimiter = $this->randomName(32);
    $values = array();
    // Set some random content for each region available.
    foreach ($block_regions as $region) {
      $first_chunk = $this->randomName(32);
      drupal_add_region_content($region, $first_chunk);
      $second_chunk = $this->randomName(32);
      drupal_add_region_content($region, $second_chunk);
      // Store the expected result for a drupal_get_region_content call for this region.
      $values[$region] = $first_chunk . $delimiter . $second_chunk;
    }

    // Ensure drupal_get_region_content returns expected results when fetching all regions.
    $content = drupal_get_region_content(NULL, $delimiter);
    foreach ($content as $region => $region_content) {
      $this->assertEqual($region_content, $values[$region], format_string('@region region text verified when fetching all regions', array('@region' => $region)));
    }

    // Ensure drupal_get_region_content returns expected results when fetching a single region.
    foreach ($block_regions as $region) {
      $region_content = drupal_get_region_content($region, $delimiter);
      $this->assertEqual($region_content, $values[$region], format_string('@region region text verified when fetching single region.', array('@region' => $region)));
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
