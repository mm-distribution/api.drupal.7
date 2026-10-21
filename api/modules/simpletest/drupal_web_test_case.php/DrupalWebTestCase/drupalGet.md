# DrupalWebTestCase::drupalGet()

- **Type:** Method
- **File:** [`modules/simpletest/drupal_web_test_case.php`](../_file.md), lines 2268–2285 · [local source](../../../../../source/modules/simpletest/drupal_web_test_case.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php#L2268-L2285)
- **Class:** [DrupalWebTestCase](../DrupalWebTestCase.md)
- **Module/theme:** simpletest

## Signature

```php
protected function drupalGet($path, array $options = array(), array $headers = array())
```

## Documentation

```text
Retrieves a Drupal path or an absolute path.

@param $path
  Drupal path or URL to load into internal browser
@param $options
  Options to be forwarded to url().
@param $headers
  An array containing additional HTTP request headers, each formatted as
  "name: value".
@return
  The retrieved HTML string, also available as $this->drupalGetContent()
```

## Code

```php
  protected function drupalGet($path, array $options = array(), array $headers = array()) {
    $options['absolute'] = TRUE;

    // We re-using a CURL connection here. If that connection still has certain
    // options set, it might change the GET into a POST. Make sure we clear out
    // previous options.
    $out = $this->curlExec(array(CURLOPT_HTTPGET => TRUE, CURLOPT_URL => url($path, $options), CURLOPT_NOBODY => FALSE, CURLOPT_HTTPHEADER => $headers));
    $this->refreshVariables(); // Ensure that any changes to variables in the other thread are picked up.

    // Replace original page output with new output from redirected page(s).
    if ($new = $this->checkForMetaRefresh()) {
      $out = $new;
    }
    $this->verbose('GET request to: ' . $path .
                   '<hr />Ending URL: ' . $this->getUrl() .
                   '<hr />' . $out);
    return $out;
  }
```

---
_Drupal 7.103 · [modules/simpletest/drupal_web_test_case.php](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php) · Licensed GPL-2.0-or-later (see LICENSE)._
