# DrupalGotoTest::testDrupalGoto()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 1459–1489 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L1459-L1489)
- **Class:** [DrupalGotoTest](../DrupalGotoTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testDrupalGoto()
```

## Documentation

```text
Test drupal_goto().
```

## Code

```php
  function testDrupalGoto() {
    $this->drupalGet('common-test/drupal_goto/redirect');
    $headers = $this->drupalGetHeaders(TRUE);
    list(, $status) = explode(' ', $headers[0][':status'], 3);
    $this->assertEqual($status, 302, 'Expected response code was sent.');
    $this->assertText('drupal_goto', 'Drupal goto redirect succeeded.');
    $this->assertEqual($this->getUrl(), url('common-test/drupal_goto', array('absolute' => TRUE)), 'Drupal goto redirected to expected URL.');

    $this->drupalGet('common-test/drupal_goto/redirect_advanced');
    $headers = $this->drupalGetHeaders(TRUE);
    list(, $status) = explode(' ', $headers[0][':status'], 3);
    $this->assertEqual($status, 301, 'Expected response code was sent.');
    $this->assertText('drupal_goto', 'Drupal goto redirect succeeded.');
    $this->assertEqual($this->getUrl(), url('common-test/drupal_goto', array('query' => array('foo' => '123'), 'absolute' => TRUE)), 'Drupal goto redirected to expected URL.');

    // Test that calling drupal_goto() on the current path is not dangerous.
    variable_set('common_test_redirect_current_path', TRUE);
    $this->drupalGet('', array('query' => array('q' => 'http://www.example.com/')));
    $headers = $this->drupalGetHeaders(TRUE);
    list(, $status) = explode(' ', $headers[0][':status'], 3);
    $this->assertEqual($status, 302, 'Expected response code was sent.');
    $this->assertNotEqual($this->getUrl(), 'http://www.example.com/', 'Drupal goto did not redirect to external URL.');
    $this->assertTrue(strpos($this->getUrl(), url('<front>', array('absolute' => TRUE))) === 0, 'Drupal redirected to itself.');
    variable_del('common_test_redirect_current_path');
    // Test that drupal_goto() respects ?destination=xxx. Use an complicated URL
    // to test that the path is encoded and decoded properly.
    $destination = 'common-test/drupal_goto/destination?foo=%2525&bar=123';
    $this->drupalGet('common-test/drupal_goto/redirect', array('query' => array('destination' => $destination)));
    $this->assertText('drupal_goto', 'Drupal goto redirect with destination succeeded.');
    $this->assertEqual($this->getUrl(), url('common-test/drupal_goto/destination', array('query' => array('foo' => '%25', 'bar' => '123'), 'absolute' => TRUE)), 'Drupal goto redirected to given query string destination.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
