# drupal_pre_render_conditional_comments()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 5832–5877 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L5832-L5877)

## Signature

```php
function drupal_pre_render_conditional_comments($elements)
```

## Documentation

```text
#pre_render callback to render #browsers into #prefix and #suffix.

@param $elements
  A render array with a '#browsers' property. The '#browsers' property can
  contain any or all of the following keys:
  - 'IE': If FALSE, the element is not rendered by Internet Explorer. If
    TRUE, the element is rendered by Internet Explorer. Can also be a string
    containing an expression for Internet Explorer to evaluate as part of a
    conditional comment. For example, this can be set to 'lt IE 7' for the
    element to be rendered in Internet Explorer 6, but not in Internet
    Explorer 7 or higher. Defaults to TRUE.
  - '!IE': If FALSE, the element is not rendered by browsers other than
    Internet Explorer. If TRUE, the element is rendered by those browsers.
    Defaults to TRUE.
  Examples:
  - To render an element in all browsers, '#browsers' can be left out or set
    to array('IE' => TRUE, '!IE' => TRUE).
  - To render an element in Internet Explorer only, '#browsers' can be set
    to array('!IE' => FALSE).
  - To render an element in Internet Explorer 6 only, '#browsers' can be set
    to array('IE' => 'lt IE 7', '!IE' => FALSE).
  - To render an element in Internet Explorer 8 and higher and in all other
    browsers, '#browsers' can be set to array('IE' => 'gte IE 8').

@return
  The passed-in element with markup for conditional comments potentially
  added to '#prefix' and '#suffix'.
```

## Code

```php
function drupal_pre_render_conditional_comments($elements) {
  $browsers = isset($elements['#browsers']) ? $elements['#browsers'] : array();
  $browsers += array(
    'IE' => TRUE,
    '!IE' => TRUE,
  );

  // If rendering in all browsers, no need for conditional comments.
  if ($browsers['IE'] === TRUE && $browsers['!IE']) {
    return $elements;
  }

  // Determine the conditional comment expression for Internet Explorer to
  // evaluate.
  if ($browsers['IE'] === TRUE) {
    $expression = 'IE';
  }
  elseif ($browsers['IE'] === FALSE) {
    $expression = '!IE';
  }
  else {
    $expression = $browsers['IE'];
  }

  // Wrap the element's potentially existing #prefix and #suffix properties with
  // conditional comment markup. The conditional comment expression is evaluated
  // by Internet Explorer only. To control the rendering by other browsers,
  // either the "downlevel-hidden" or "downlevel-revealed" technique must be
  // used. See http://en.wikipedia.org/wiki/Conditional_comment for details.
  $elements += array(
    '#prefix' => '',
    '#suffix' => '',
  );
  if (!$browsers['!IE']) {
    // "downlevel-hidden".
    $elements['#prefix'] = "\n<!--[if $expression]>\n" . $elements['#prefix'];
    $elements['#suffix'] .= "<![endif]-->\n";
  }
  else {
    // "downlevel-revealed".
    $elements['#prefix'] = "\n<!--[if $expression]><!-->\n" . $elements['#prefix'];
    $elements['#suffix'] .= "<!--<![endif]-->\n";
  }

  return $elements;
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
