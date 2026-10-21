# format_rss_item()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 1823–1832 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L1823-L1832)
- **Topics:** [format](../../topics/format.md)

## Signature

```php
function format_rss_item($title, $link, $description, $args = array())
```

## Documentation

```text
Formats a single RSS item.

Arbitrary elements may be added using the $args associative array.
```

## Code

```php
function format_rss_item($title, $link, $description, $args = array()) {
  $output = "<item>\n";
  $output .= ' <title>' . check_plain($title) . "</title>\n";
  $output .= ' <link>' . check_url($link) . "</link>\n";
  $output .= ' <description>' . check_plain($description) . "</description>\n";
  $output .= format_xml_elements($args);
  $output .= "</item>\n";

  return $output;
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
