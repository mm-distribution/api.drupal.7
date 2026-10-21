# format_rss_channel()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 1798–1816 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L1798-L1816)
- **Topics:** [format](../../topics/format.md)

## Signature

```php
function format_rss_channel($title, $link, $description, $items, $langcode = NULL, $args = array())
```

## Documentation

```text
Formats an RSS channel.

Arbitrary elements may be added using the $args associative array.
```

## Code

```php
function format_rss_channel($title, $link, $description, $items, $langcode = NULL, $args = array()) {
  global $language_content;
  $langcode = $langcode ? $langcode : $language_content->language;

  $output = "<channel>\n";
  $output .= ' <title>' . check_plain($title) . "</title>\n";
  $output .= ' <link>' . check_url($link) . "</link>\n";

  // The RSS 2.0 "spec" doesn't indicate HTML can be used in the description.
  // We strip all HTML tags, but need to prevent double encoding from properly
  // escaped source data (such as &amp becoming &amp;amp;).
  $output .= ' <description>' . check_plain(decode_entities(strip_tags($description))) . "</description>\n";
  $output .= ' <language>' . check_plain($langcode) . "</language>\n";
  $output .= format_xml_elements($args);
  $output .= $items;
  $output .= "</channel>\n";

  return $output;
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
