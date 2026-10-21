# CommonURLUnitTest::testExternalUrls()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 351–392 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L351-L392)
- **Class:** [CommonURLUnitTest](../CommonURLUnitTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testExternalUrls()
```

## Documentation

```text
Test external URL handling.
```

## Code

```php
  function testExternalUrls() {
    $test_url = 'http://drupal.org/';

    // Verify external URL can contain a fragment.
    $url = $test_url . '#drupal';
    $result = url($url);
    $this->assertEqual($url, $result, 'External URL with fragment works without a fragment in $options.');

    // Verify fragment can be overidden in an external URL.
    $url = $test_url . '#drupal';
    $fragment = $this->randomName(10);
    $result = url($url, array('fragment' => $fragment));
    $this->assertEqual($test_url . '#' . $fragment, $result, 'External URL fragment is overidden with a custom fragment in $options.');

    // Verify external URL can contain a query string.
    $url = $test_url . '?drupal=awesome';
    $result = url($url);
    $this->assertEqual($url, $result, 'External URL with query string works without a query string in $options.');

    // Verify external URL can be extended with a query string.
    $url = $test_url;
    $query = array($this->randomName(5) => $this->randomName(5));
    $result = url($url, array('query' => $query));
    $this->assertEqual($url . '?' . http_build_query($query, '', '&'), $result, 'External URL can be extended with a query string in $options.');

    // Verify query string can be extended in an external URL.
    $url = $test_url . '?drupal=awesome';
    $query = array($this->randomName(5) => $this->randomName(5));
    $result = url($url, array('query' => $query));
    $this->assertEqual($url . '&' . http_build_query($query, '', '&'), $result, 'External URL query string can be extended with a custom query string in $options.');

    // Verify that an internal URL does not result in an external URL without
    // protocol part.
    $url = '/drupal.org';
    $result = url($url);
    $this->assertTrue(strpos($result, '//') === FALSE, 'Internal URL does not turn into an external URL.');

    // Verify that an external URL without protocol part is recognized as such.
    $url = '//drupal.org';
    $result = url($url);
    $this->assertEqual($url, $result, 'External URL without protocol is not altered.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
