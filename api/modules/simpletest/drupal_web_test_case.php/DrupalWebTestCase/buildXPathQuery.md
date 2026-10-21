# DrupalWebTestCase::buildXPathQuery()

- **Type:** Method
- **File:** [`modules/simpletest/drupal_web_test_case.php`](../_file.md), lines 2888–2909 · [local source](../../../../../source/modules/simpletest/drupal_web_test_case.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php#L2888-L2909)
- **Class:** [DrupalWebTestCase](../DrupalWebTestCase.md)
- **Module/theme:** simpletest

## Signature

```php
protected function buildXPathQuery($xpath, array $args = array())
```

## Documentation

```text
Builds an XPath query.

Builds an XPath query by replacing placeholders in the query by the value
of the arguments.

XPath 1.0 (the version supported by libxml2, the underlying XML library
used by PHP) doesn't support any form of quotation. This function
simplifies the building of XPath expression.

@param $xpath
  An XPath query, possibly with placeholders in the form ':name'.
@param $args
  An array of arguments with keys in the form ':name' matching the
  placeholders in the query. The values may be either strings or numeric
  values.
@return
  An XPath query with arguments replaced.
```

## Code

```php
  protected function buildXPathQuery($xpath, array $args = array()) {
    // Replace placeholders.
    foreach ($args as $placeholder => $value) {
      // XPath 1.0 doesn't support a way to escape single or double quotes in a
      // string literal. We split double quotes out of the string, and encode
      // them separately.
      if (is_string($value)) {
        // Explode the text at the quote characters.
        $parts = explode('"', $value);

        // Quote the parts.
        foreach ($parts as &$part) {
          $part = '"' . $part . '"';
        }

        // Return the string.
        $value = count($parts) > 1 ? 'concat(' . implode(', \'"\', ', $parts) . ')' : $parts[0];
      }
      $xpath = preg_replace('/' . preg_quote($placeholder) . '\b/', $value, $xpath);
    }
    return $xpath;
  }
```

---
_Drupal 7.103 · [modules/simpletest/drupal_web_test_case.php](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php) · Licensed GPL-2.0-or-later (see LICENSE)._
