# theme_feed_icon()

- **Type:** Function
- **File:** [`includes/theme.inc`](_file.md), lines 2291–2296 · [local source](../../../source/includes/theme.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/theme.inc#L2291-L2296)
- **Topics:** [themeable](../../topics/themeable.md)

## Signature

```php
function theme_feed_icon($variables)
```

## Documentation

```text
Returns HTML for a feed icon.

@param $variables
  An associative array containing:
  - url: An internal system path or a fully qualified external URL of the
    feed.
  - title: A descriptive title of the feed.
```

## Code

```php
function theme_feed_icon($variables) {
  $text = t('Subscribe to !feed-title', array('!feed-title' => $variables['title']));
  if ($image = theme('image', array('path' => 'misc/feed.png', 'width' => 16, 'height' => 16, 'alt' => $text))) {
    return l($image, $variables['url'], array('html' => TRUE, 'attributes' => array('class' => array('feed-icon'), 'title' => $text)));
  }
}
```

---
_Drupal 7.103 · [includes/theme.inc](https://github.com/drupal/drupal/blob/7.103/includes/theme.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
