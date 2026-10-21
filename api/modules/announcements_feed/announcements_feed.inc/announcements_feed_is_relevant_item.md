# announcements_feed_is_relevant_item()

- **Type:** Function
- **File:** [`modules/announcements_feed/announcements_feed.inc`](_file.md), lines 178–211 · [local source](../../../../source/modules/announcements_feed/announcements_feed.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/announcements_feed/announcements_feed.inc#L178-L211)
- **Module/theme:** announcements_feed

## Signature

```php
function announcements_feed_is_relevant_item($version)
```

## Documentation

```text
Check whether the version given is relevant to the Drupal version used.

@param string $version
  Version to check.

@return bool
  Return TRUE if the version matches Drupal version.
```

## Code

```php
function announcements_feed_is_relevant_item($version) {
  if ($version == '*') {
    return TRUE;
  }
  // Split the version if received in || formats.
  $version_patterns = '/\|\|/';
  $all_versions = preg_split($version_patterns, $version);
  // The operation is optional and defaults to equals.
  $p_op = '(?P<operation>!=|\^|==|=|<|<=|>|>=|<>)?';
  $operations = '=';
  // Extracts major version from version string like 7, 8, 9.
  $p_major = '(?P<major>\d+)';
  // Extracts minor version from version string.
  $p_minor = '(?P<minor>(?:\d+|x)(?:-[A-Za-z]+\d+)?)';
  foreach ($all_versions as $version) {
    if (preg_match("/^\s*$p_op\s*$p_major(\.$p_minor)?/", $version, $matches)) {
      $feed_version = $matches['major'];
      if (!empty($matches['minor'])) {
        $feed_version = $matches['major'] . '.' . $matches['minor'];
      }
      if (!empty($matches['operation'])) {
        $operations = $matches['operation'];
        if ($operations == '^') {
          $operations = '>=';
        }
      }
      if (isset($operations) && version_compare(VERSION, $feed_version, $operations)) {
        return TRUE;
      }
    }
  }

  return FALSE;
}
```

---
_Drupal 7.103 · [modules/announcements_feed/announcements_feed.inc](https://github.com/drupal/drupal/blob/7.103/modules/announcements_feed/announcements_feed.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
