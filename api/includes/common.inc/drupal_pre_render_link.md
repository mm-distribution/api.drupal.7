# drupal_pre_render_link()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 5893–5931 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L5893-L5931)

## Signature

```php
function drupal_pre_render_link($element)
```

## Documentation

```text
#pre_render callback to render a link into #markup.

Doing so during pre_render gives modules a chance to alter the link parts.

@param $elements
  A structured array whose keys form the arguments to l():
  - #title: The link text to pass as argument to l().
  - #href: The URL path component to pass as argument to l().
  - #options: (optional) An array of options to pass to l().

@return
  The passed-in elements containing a rendered link in '#markup'.
```

## Code

```php
function drupal_pre_render_link($element) {
  // By default, link options to pass to l() are normally set in #options.
  $element += array('#options' => array());
  // However, within the scope of renderable elements, #attributes is a valid
  // way to specify attributes, too. Take them into account, but do not override
  // attributes from #options.
  if (isset($element['#attributes'])) {
    $element['#options'] += array('attributes' => array());
    $element['#options']['attributes'] += $element['#attributes'];
  }

  // This #pre_render callback can be invoked from inside or outside of a Form
  // API context, and depending on that, a HTML ID may be already set in
  // different locations. #options should have precedence over Form API's #id.
  // #attributes have been taken over into #options above already.
  if (isset($element['#options']['attributes']['id'])) {
    $element['#id'] = $element['#options']['attributes']['id'];
  }
  elseif (isset($element['#id'])) {
    $element['#options']['attributes']['id'] = $element['#id'];
  }

  // Conditionally invoke ajax_pre_render_element(), if #ajax is set.
  if (isset($element['#ajax']) && !isset($element['#ajax_processed'])) {
    // If no HTML ID was found above, automatically create one.
    if (!isset($element['#id'])) {
      $element['#id'] = $element['#options']['attributes']['id'] = drupal_html_id('ajax-link');
    }
    // If #ajax['path] was not specified, use the href as Ajax request URL.
    if (!isset($element['#ajax']['path'])) {
      $element['#ajax']['path'] = $element['#href'];
      $element['#ajax']['options'] = $element['#options'];
    }
    $element = ajax_pre_render_element($element);
  }

  $element['#markup'] = l($element['#title'], $element['#href'], $element['#options']);
  return $element;
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
