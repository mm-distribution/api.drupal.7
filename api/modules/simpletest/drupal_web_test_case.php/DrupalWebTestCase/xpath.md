# DrupalWebTestCase::xpath()

- **Type:** Method
- **File:** [`modules/simpletest/drupal_web_test_case.php`](../_file.md), lines 2927–2939 · [local source](../../../../../source/modules/simpletest/drupal_web_test_case.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php#L2927-L2939)
- **Class:** [DrupalWebTestCase](../DrupalWebTestCase.md)
- **Module/theme:** simpletest

## Signature

```php
protected function xpath($xpath, array $arguments = array())
```

## Documentation

```text
Perform an xpath search on the contents of the internal browser. The search
is relative to the root element (HTML tag normally) of the page.

@param $xpath
  The xpath string to use in the search.
@param array $arguments
  An array of arguments with keys in the form ':name' matching the
  placeholders in the query. The values may be either strings or numeric
  values.

@return
  The return value of the xpath search. For details on the xpath string
  format and return values see the SimpleXML documentation,
  http://us.php.net/manual/function.simplexml-element-xpath.php.
```

## Code

```php
  protected function xpath($xpath, array $arguments = array()) {
    if ($this->parse()) {
      $xpath = $this->buildXPathQuery($xpath, $arguments);
      $result = $this->elements->xpath($xpath);
      // Some combinations of PHP / libxml versions return an empty array
      // instead of the documented FALSE. Forcefully convert any falsish values
      // to an empty array to allow foreach(...) constructions.
      return $result ? $result : array();
    }
    else {
      return FALSE;
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/drupal_web_test_case.php](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php) · Licensed GPL-2.0-or-later (see LICENSE)._
