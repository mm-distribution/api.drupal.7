# DrupalWebTestCase::drupalHead()

- **Type:** Method
- **File:** [`modules/simpletest/drupal_web_test_case.php`](../_file.md), lines 2709–2714 · [local source](../../../../../source/modules/simpletest/drupal_web_test_case.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php#L2709-L2714)
- **Class:** [DrupalWebTestCase](../DrupalWebTestCase.md)
- **Module/theme:** simpletest

## Signature

```php
protected function drupalHead($path, array $options = array(), array $headers = array())
```

## Documentation

```text
Retrieves only the headers for a Drupal path or an absolute path.

@param $path
  Drupal path or URL to load into internal browser
@param $options
  Options to be forwarded to url().
@param $headers
  An array containing additional HTTP request headers, each formatted as
  "name: value".
@return
  The retrieved headers, also available as $this->drupalGetContent()
```

## Code

```php
  protected function drupalHead($path, array $options = array(), array $headers = array()) {
    $options['absolute'] = TRUE;
    $out = $this->curlExec(array(CURLOPT_NOBODY => TRUE, CURLOPT_URL => url($path, $options), CURLOPT_HTTPHEADER => $headers));
    $this->refreshVariables(); // Ensure that any changes to variables in the other thread are picked up.
    return $out;
  }
```

---
_Drupal 7.103 · [modules/simpletest/drupal_web_test_case.php](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php) · Licensed GPL-2.0-or-later (see LICENSE)._
