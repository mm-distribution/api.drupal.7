# _block_compare()

- **Type:** Function
- **File:** [`modules/block/block.admin.inc`](_file.md), lines 204–239 · [local source](../../../../source/modules/block/block.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.admin.inc#L204-L239)
- **Module/theme:** block

## Signature

```php
function _block_compare($a, $b)
```

## Documentation

```text
Sorts active blocks by region, then by weight; sorts inactive blocks by name.

Callback for usort() in block_admin_display_prepare_blocks().
```

## Code

```php
function _block_compare($a, $b) {
  global $theme_key;

  // Theme should be set before calling this function, or the current theme
  // is being used.
  $theme = &drupal_static(__FUNCTION__ . ':theme');
  if (!isset($theme)) {
    $theme = $theme_key;
  }

  $regions = &drupal_static(__FUNCTION__ . ':regions');
  // We need the region list to correctly order by region.
  if (!isset($regions)) {
    $regions = array_flip(array_keys(system_region_list($theme)));
    $regions[BLOCK_REGION_NONE] = count($regions);
  }

  // Separate enabled from disabled.
  $status = $b['status'] - $a['status'];
  if ($status) {
    return $status;
  }
  // Sort by region (in the order defined by theme .info file).
  if ((!empty($a['region']) && !empty($b['region'])) && ($place = ($regions[$a['region']] - $regions[$b['region']]))) {
    return $place;
  }
  // Sort by weight, unless disabled.
  if ($a['region'] != BLOCK_REGION_NONE) {
    $weight = $a['weight'] - $b['weight'];
    if ($weight) {
      return $weight;
    }
  }
  // Sort by title.
  return strcmp($a['info'], $b['info']);
}
```

---
_Drupal 7.103 · [modules/block/block.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/block/block.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
