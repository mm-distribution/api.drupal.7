# text_summary()

- **Type:** Function
- **File:** [`modules/field/modules/text/text.module`](_file.md), lines 352–455 · [local source](../../../../../../source/modules/field/modules/text/text.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/text/text.module#L352-L455)
- **Module/theme:** text

## Signature

```php
function text_summary($text, $format = NULL, $size = NULL)
```

## Documentation

```text
Generate a trimmed, formatted version of a text field value.

If the end of the summary is not indicated using the <!--break--> delimiter
then we generate the summary automatically, trying to end it at a sensible
place such as the end of a paragraph, a line break, or the end of a
sentence (in that order of preference).

@param $text
  The content for which a summary will be generated.
@param $format
  The format of the content.
  If the PHP filter is present and $text contains PHP code, we do not
  split it up to prevent parse errors.
  If the line break filter is present then we treat newlines embedded in
  $text as line breaks.
  If the htmlcorrector filter is present, it will be run on the generated
  summary (if different from the incoming $text).
@param $size
  The desired character length of the summary. If omitted, the default
  value will be used. Ignored if the special delimiter is present
  in $text.
@return
  The generated summary.
```

## Code

```php
function text_summary($text, $format = NULL, $size = NULL) {

  // If the input text is NULL, return unchanged.
  if (is_null($text)) {
    return NULL;
  }

  if (!isset($size)) {
    // What used to be called 'teaser' is now called 'summary', but
    // the variable 'teaser_length' is preserved for backwards compatibility.
    $size = variable_get('teaser_length', 600);
  }

  // Find where the delimiter is in the body
  $delimiter = strpos($text, '<!--break-->');

  // If the size is zero, and there is no delimiter, the entire body is the summary.
  if ($size == 0 && $delimiter === FALSE) {
    return $text;
  }

  // If a valid delimiter has been specified, use it to chop off the summary.
  if ($delimiter !== FALSE) {
    return substr($text, 0, $delimiter);
  }

  // We check for the presence of the PHP evaluator filter in the current
  // format. If the body contains PHP code, we do not split it up to prevent
  // parse errors.
  if (isset($format)) {
    $filters = filter_list_format($format);
    if (isset($filters['php_code']) && $filters['php_code']->status && strpos($text, '<?') !== FALSE) {
      return $text;
    }
  }

  // If we have a short body, the entire body is the summary.
  if (drupal_strlen($text) <= $size) {
    return $text;
  }

  // If the delimiter has not been specified, try to split at paragraph or
  // sentence boundaries.

  // The summary may not be longer than maximum length specified. Initial slice.
  $summary = truncate_utf8($text, $size);

  // Store the actual length of the UTF8 string -- which might not be the same
  // as $size.
  $max_rpos = strlen($summary);

  // How much to cut off the end of the summary so that it doesn't end in the
  // middle of a paragraph, sentence, or word.
  // Initialize it to maximum in order to find the minimum.
  $min_rpos = $max_rpos;

  // Store the reverse of the summary. We use strpos on the reversed needle and
  // haystack for speed and convenience.
  $reversed = strrev($summary);

  // Build an array of arrays of break points grouped by preference.
  $break_points = array();

  // A paragraph near the end of sliced summary is most preferable.
  $break_points[] = array('</p>' => 0);

  // If no complete paragraph then treat line breaks as paragraphs.
  $line_breaks = array('<br />' => 6, '<br>' => 4);
  // Newline only indicates a line break if line break converter
  // filter is present.
  if (isset($filters['filter_autop'])) {
    $line_breaks["\n"] = 1;
  }
  $break_points[] = $line_breaks;

  // If the first paragraph is too long, split at the end of a sentence.
  $break_points[] = array('. ' => 1, '! ' => 1, '? ' => 1, '。' => 0, '؟ ' => 1);

  // Iterate over the groups of break points until a break point is found.
  foreach ($break_points as $points) {
    // Look for each break point, starting at the end of the summary.
    foreach ($points as $point => $offset) {
      // The summary is already reversed, but the break point isn't.
      $rpos = strpos($reversed, strrev($point));
      if ($rpos !== FALSE) {
        $min_rpos = min($rpos + $offset, $min_rpos);
      }
    }

    // If a break point was found in this group, slice and stop searching.
    if ($min_rpos !== $max_rpos) {
      // Don't slice with length 0. Length must be <0 to slice from RHS.
      $summary = ($min_rpos === 0) ? $summary : substr($summary, 0, 0 - $min_rpos);
      break;
    }
  }

  // If the htmlcorrector filter is present, apply it to the generated summary.
  if (isset($filters['filter_htmlcorrector'])) {
    $summary = _filter_htmlcorrector($summary);
  }

  return $summary;
}
```

---
_Drupal 7.103 · [modules/field/modules/text/text.module](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/text/text.module) · Licensed GPL-2.0-or-later (see LICENSE)._
