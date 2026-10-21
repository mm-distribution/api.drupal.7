# SimpleTestBrowserTestCase::testGetAbsoluteUrl()

- **Type:** Method
- **File:** [`modules/simpletest/simpletest.test`](../_file.md), lines 374–393 · [local source](../../../../../source/modules/simpletest/simpletest.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.test#L374-L393)
- **Class:** [SimpleTestBrowserTestCase](../SimpleTestBrowserTestCase.md)
- **Module/theme:** simpletest

## Signature

```php
function testGetAbsoluteUrl()
```

## Documentation

```text
Test DrupalWebTestCase::getAbsoluteUrl().
```

## Code

```php
  function testGetAbsoluteUrl() {
    // Testbed runs with Clean URLs disabled, so disable it here.
    variable_set('clean_url', 0);
    $url = 'user/login';

    $this->drupalGet($url);
    $absolute = url($url, array('absolute' => TRUE));
    $this->assertEqual($absolute, $this->url, 'Passed and requested URL are equal.');
    $this->assertEqual($this->url, $this->getAbsoluteUrl($this->url), 'Requested and returned absolute URL are equal.');

    $this->drupalPost(NULL, array(), t('Log in'));
    $this->assertEqual($absolute, $this->url, 'Passed and requested URL are equal.');
    $this->assertEqual($this->url, $this->getAbsoluteUrl($this->url), 'Requested and returned absolute URL are equal.');

    $this->clickLink('Create new account');
    $url = 'user/register';
    $absolute = url($url, array('absolute' => TRUE));
    $this->assertEqual($absolute, $this->url, 'Passed and requested URL are equal.');
    $this->assertEqual($this->url, $this->getAbsoluteUrl($this->url), 'Requested and returned absolute URL are equal.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/simpletest.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.test) · Licensed GPL-2.0-or-later (see LICENSE)._
