# format_interval()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 2027–2051 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L2027-L2051)
- **Topics:** [format](../../topics/format.md)

## Signature

```php
function format_interval($interval, $granularity = 2, $langcode = NULL)
```

## Documentation

```text
Formats a time interval with the requested granularity.

@param $interval
  The length of the interval in seconds.
@param $granularity
  How many different units to display in the string.
@param $langcode
  Optional language code to translate to a language other than
  what is used to display the page.

@return
  A translated string representation of the interval.
```

## Code

```php
function format_interval($interval, $granularity = 2, $langcode = NULL) {
  $units = array(
    '1 year|@count years' => 31536000,
    '1 month|@count months' => 2592000,
    '1 week|@count weeks' => 604800,
    '1 day|@count days' => 86400,
    '1 hour|@count hours' => 3600,
    '1 min|@count min' => 60,
    '1 sec|@count sec' => 1
  );
  $output = '';
  foreach ($units as $key => $value) {
    $key = explode('|', $key);
    if ($interval >= $value) {
      $output .= ($output ? ' ' : '') . format_plural(floor($interval / $value), $key[0], $key[1], array(), array('langcode' => $langcode));
      $interval = (int) $interval % $value;
      $granularity--;
    }

    if ($granularity == 0) {
      break;
    }
  }
  return $output ? $output : t('0 sec', array(), array('langcode' => $langcode));
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
