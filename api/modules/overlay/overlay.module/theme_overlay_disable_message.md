# theme_overlay_disable_message()

- **Type:** Function
- **File:** [`modules/overlay/overlay.module`](_file.md), lines 419–444 · [local source](../../../../source/modules/overlay/overlay.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/overlay/overlay.module#L419-L444)
- **Module/theme:** overlay
- **Topics:** [themeable](../../../topics/themeable.md)

## Signature

```php
function theme_overlay_disable_message($variables)
```

## Documentation

```text
Returns the HTML for the message about how to disable the overlay.

@param $variables
  An associative array with an 'element' element, which itself is an
  associative array containing:
  - profile_link: The link to this user's account.
  - dismiss_message_link: The link to dismiss the overlay.

@ingroup themeable
```

## Code

```php
function theme_overlay_disable_message($variables) {
  $element = $variables['element'];

  // Add CSS classes to hide the links from most sighted users, while keeping
  // them accessible to screen-reader users and keyboard-only users. To assist
  // screen-reader users, this message appears in both the parent and child
  // documents, but only the one in the child document is part of the tab order.
  foreach (array('profile_link', 'dismiss_message_link') as $key) {
    $element[$key]['#options']['attributes']['class'][] = 'element-invisible';
    if (overlay_get_mode() == 'child') {
      $element[$key]['#options']['attributes']['class'][] = 'element-focusable';
    }
  }

  // Render the links.
  $output = drupal_render($element['profile_link']) . ' ' . drupal_render($element['dismiss_message_link']);

  // Add a heading for screen-reader users. The heading doesn't need to be seen
  // by sighted users.
  $output = '<h3 class="element-invisible">' . t('Options for the administrative overlay') . '</h3>' . $output;

  // Wrap in a container for styling.
  $output = '<div id="overlay-disable-message" class="clearfix">' . $output . '</div>';

  return $output;
}
```

---
_Drupal 7.103 · [modules/overlay/overlay.module](https://github.com/drupal/drupal/blob/7.103/modules/overlay/overlay.module) · Licensed GPL-2.0-or-later (see LICENSE)._
