# theme_aggregator_page_opml()

- **Type:** Function
- **File:** [`modules/aggregator/aggregator.pages.inc`](_file.md), lines 500–519 · [local source](../../../../source/modules/aggregator/aggregator.pages.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.pages.inc#L500-L519)
- **Module/theme:** aggregator
- **Topics:** [themeable](../../../topics/themeable.md)

## Signature

```php
function theme_aggregator_page_opml($variables)
```

## Documentation

```text
Prints the OPML page for the feed.

@param $variables
  An associative array containing:
  - feeds: An array of the feeds to theme.

@ingroup themeable
```

## Code

```php
function theme_aggregator_page_opml($variables) {
  $feeds = $variables['feeds'];

  drupal_add_http_header('Content-Type', 'text/xml; charset=utf-8');

  $output  = "<?xml version=\"1.0\" encoding=\"utf-8\"?>\n";
  $output .= "<opml version=\"1.1\">\n";
  $output .= "<head>\n";
  $output .= '<title>' . check_plain(variable_get('site_name', 'Drupal')) . "</title>\n";
  $output .= '<dateModified>' . gmdate(DATE_RFC2822, REQUEST_TIME) . "</dateModified>\n";
  $output .= "</head>\n";
  $output .= "<body>\n";
  foreach ($feeds as $feed) {
    $output .= '<outline text="' . check_plain($feed->title) . '" xmlUrl="' . check_url($feed->url) . "\" />\n";
  }
  $output .= "</body>\n";
  $output .= "</opml>\n";

  print $output;
}
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.pages.inc](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.pages.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
