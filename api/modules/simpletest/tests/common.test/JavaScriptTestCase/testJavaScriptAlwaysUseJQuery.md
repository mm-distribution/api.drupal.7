# JavaScriptTestCase::testJavaScriptAlwaysUseJQuery()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 1671–1787 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L1671-L1787)
- **Class:** [JavaScriptTestCase](../JavaScriptTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testJavaScriptAlwaysUseJQuery()
```

## Documentation

```text
Test the 'javascript_always_use_jquery' variable.
```

## Code

```php
  function testJavaScriptAlwaysUseJQuery() {
    // The default front page of the site should use jQuery and other standard
    // scripts and settings.
    $this->drupalGet('');
    $this->assertRaw('misc/jquery.js', 'Default behavior: The front page of the site includes jquery.js.');
    $this->assertRaw('misc/drupal.js', 'Default behavior: The front page of the site includes drupal.js.');
    $this->assertRaw('Drupal.settings', 'Default behavior: The front page of the site includes Drupal settings.');
    $this->assertRaw('basePath', 'Default behavior: The front page of the site includes the basePath Drupal setting.');

    // The default front page should not use jQuery and other standard scripts
    // and settings when the 'javascript_always_use_jquery' variable is set to
    // FALSE.
    variable_set('javascript_always_use_jquery', FALSE);
    $this->drupalGet('');
    $this->assertNoRaw('misc/jquery.js', 'When "javascript_always_use_jquery" is FALSE: The front page of the site does not include jquery.js.');
    $this->assertNoRaw('misc/drupal.js', 'When "javascript_always_use_jquery" is FALSE: The front page of the site does not include drupal.js.');
    $this->assertNoRaw('Drupal.settings', 'When "javascript_always_use_jquery" is FALSE: The front page of the site does not include Drupal settings.');
    $this->assertNoRaw('basePath', 'When "javascript_always_use_jquery" is FALSE: The front page of the site does not include the basePath Drupal setting.');
    variable_del('javascript_always_use_jquery');

    // When only settings have been added via drupal_add_js(), drupal_get_js()
    // should still return jQuery and other standard scripts and settings.
    $this->resetStaticVariables();
    drupal_add_js(array('testJavaScriptSetting' => 'test'), 'setting');
    $javascript = drupal_get_js();
    $this->assertTrue(strpos($javascript, 'misc/jquery.js') !== FALSE, 'Default behavior: The JavaScript returned by drupal_get_js() when only settings have been added includes jquery.js.');
    $this->assertTrue(strpos($javascript, 'misc/drupal.js') !== FALSE, 'Default behavior: The JavaScript returned by drupal_get_js() when only settings have been added includes drupal.js.');
    $this->assertTrue(strpos($javascript, 'Drupal.settings') !== FALSE, 'Default behavior: The JavaScript returned by drupal_get_js() when only settings have been added includes Drupal.settings.');
    $this->assertTrue(strpos($javascript, 'basePath') !== FALSE, 'Default behavior: The JavaScript returned by drupal_get_js() when only settings have been added includes the basePath Drupal setting.');
    $this->assertTrue(strpos($javascript, 'testJavaScriptSetting') !== FALSE, 'Default behavior: The JavaScript returned by drupal_get_js() when only settings have been added includes the added Drupal settings.');

    // When only settings have been added via drupal_add_js() and the
    // 'javascript_always_use_jquery' variable is set to FALSE, drupal_get_js()
    // should not return jQuery and other standard scripts and settings, nor
    // should it return the requested settings (since they cannot actually be
    // addded to the page without jQuery).
    $this->resetStaticVariables();
    variable_set('javascript_always_use_jquery', FALSE);
    drupal_add_js(array('testJavaScriptSetting' => 'test'), 'setting');
    $javascript = drupal_get_js();
    $this->assertTrue(strpos($javascript, 'misc/jquery.js') === FALSE, 'When "javascript_always_use_jquery" is FALSE: The JavaScript returned by drupal_get_js() when only settings have been added does not include jquery.js.');
    $this->assertTrue(strpos($javascript, 'misc/drupal.js') === FALSE, 'When "javascript_always_use_jquery" is FALSE: The JavaScript returned by drupal_get_js() when only settings have been added does not include drupal.js.');
    $this->assertTrue(strpos($javascript, 'Drupal.settings') === FALSE, 'When "javascript_always_use_jquery" is FALSE: The JavaScript returned by drupal_get_js() when only settings have been added does not include Drupal.settings.');
    $this->assertTrue(strpos($javascript, 'basePath') === FALSE, 'When "javascript_always_use_jquery" is FALSE: The JavaScript returned by drupal_get_js() when only settings have been added does not include the basePath Drupal setting.');
    $this->assertTrue(strpos($javascript, 'testJavaScriptSetting') === FALSE, 'When "javascript_always_use_jquery" is FALSE: The JavaScript returned by drupal_get_js() when only settings have been added does not include the added Drupal settings.');
    variable_del('javascript_always_use_jquery');

    // When a regular file has been added via drupal_add_js(), drupal_get_js()
    // should return jQuery and other standard scripts and settings.
    $this->resetStaticVariables();
    drupal_add_js('misc/collapse.js');
    $javascript = drupal_get_js();
    $this->assertTrue(strpos($javascript, 'misc/jquery.js') !== FALSE, 'Default behavior: The JavaScript returned by drupal_get_js() when a custom JavaScript file has been added includes jquery.js.');
    $this->assertTrue(strpos($javascript, 'misc/drupal.js') !== FALSE, 'Default behavior: The JavaScript returned by drupal_get_js() when a custom JavaScript file has been added includes drupal.js.');
    $this->assertTrue(strpos($javascript, 'Drupal.settings') !== FALSE, 'Default behavior: The JavaScript returned by drupal_get_js() when a custom JavaScript file has been added includes Drupal.settings.');
    $this->assertTrue(strpos($javascript, 'basePath') !== FALSE, 'Default behavior: The JavaScript returned by drupal_get_js() when a custom JavaScript file has been added includes the basePath Drupal setting.');
    $this->assertTrue(strpos($javascript, 'misc/collapse.js') !== FALSE, 'Default behavior: The JavaScript returned by drupal_get_js() when a custom JavaScript file has been added includes the custom file.');

    // When a regular file has been added via drupal_add_js() and the
    // 'javascript_always_use_jquery' variable is set to FALSE, drupal_get_js()
    // should still return jQuery and other standard scripts and settings
    // (since the file is assumed to require jQuery by default).
    $this->resetStaticVariables();
    variable_set('javascript_always_use_jquery', FALSE);
    drupal_add_js('misc/collapse.js');
    $javascript = drupal_get_js();
    $this->assertTrue(strpos($javascript, 'misc/jquery.js') !== FALSE, 'When "javascript_always_use_jquery" is FALSE: The JavaScript returned by drupal_get_js() when a custom JavaScript file has been added includes jquery.js.');
    $this->assertTrue(strpos($javascript, 'misc/drupal.js') !== FALSE, 'When "javascript_always_use_jquery" is FALSE: The JavaScript returned by drupal_get_js() when a custom JavaScript file has been added includes drupal.js.');
    $this->assertTrue(strpos($javascript, 'Drupal.settings') !== FALSE, 'When "javascript_always_use_jquery" is FALSE: The JavaScript returned by drupal_get_js() when a custom JavaScript file has been added includes Drupal.settings.');
    $this->assertTrue(strpos($javascript, 'basePath') !== FALSE, 'When "javascript_always_use_jquery" is FALSE: The JavaScript returned by drupal_get_js() when a custom JavaScript file has been added includes the basePath Drupal setting.');
    $this->assertTrue(strpos($javascript, 'misc/collapse.js') !== FALSE, 'When "javascript_always_use_jquery" is FALSE: The JavaScript returned by drupal_get_js() when a custom JavaScript file has been added includes the custom file.');
    variable_del('javascript_always_use_jquery');

    // When a file that does not require jQuery has been added via
    // drupal_add_js(), drupal_get_js() should still return jQuery and other
    // standard scripts and settings by default.
    $this->resetStaticVariables();
    drupal_add_js('misc/collapse.js', array('requires_jquery' => FALSE));
    $javascript = drupal_get_js();
    $this->assertTrue(strpos($javascript, 'misc/jquery.js') !== FALSE, 'Default behavior: The JavaScript returned by drupal_get_js() when a custom JavaScript file that does not require jQuery has been added includes jquery.js.');
    $this->assertTrue(strpos($javascript, 'misc/drupal.js') !== FALSE, 'Default behavior: The JavaScript returned by drupal_get_js() when a custom JavaScript file that does not require jQuery has been added includes drupal.js.');
    $this->assertTrue(strpos($javascript, 'Drupal.settings') !== FALSE, 'Default behavior: The JavaScript returned by drupal_get_js() when a custom JavaScript file that does not require jQuery has been added includes Drupal.settings.');
    $this->assertTrue(strpos($javascript, 'basePath') !== FALSE, 'Default behavior: The JavaScript returned by drupal_get_js() when a custom JavaScript file that does not require jQuery has been added includes the basePath Drupal setting.');
    $this->assertTrue(strpos($javascript, 'misc/collapse.js') !== FALSE, 'Default behavior: The JavaScript returned by drupal_get_js() when a custom JavaScript file that does not require jQuery has been added includes the custom file.');

    // When a file that does not require jQuery has been added via
    // drupal_add_js() and the 'javascript_always_use_jquery' variable is set
    // to FALSE, drupal_get_js() should not return jQuery and other standard
    // scripts and setting, but it should still return the requested file.
    $this->resetStaticVariables();
    variable_set('javascript_always_use_jquery', FALSE);
    drupal_add_js('misc/collapse.js', array('requires_jquery' => FALSE));
    $javascript = drupal_get_js();
    $this->assertTrue(strpos($javascript, 'misc/jquery.js') === FALSE, 'When "javascript_always_use_jquery" is FALSE: The JavaScript returned by drupal_get_js() when a custom JavaScript file that does not require jQuery has been added does not include jquery.js.');
    $this->assertTrue(strpos($javascript, 'misc/drupal.js') === FALSE, 'When "javascript_always_use_jquery" is FALSE: The JavaScript returned by drupal_get_js() when a custom JavaScript file that does not require jQuery has been added does not include drupal.js.');
    $this->assertTrue(strpos($javascript, 'Drupal.settings') === FALSE, 'When "javascript_always_use_jquery" is FALSE: The JavaScript returned by drupal_get_js() when a custom JavaScript file that does not require jQuery has been added does not include Drupal.settings.');
    $this->assertTrue(strpos($javascript, 'basePath') === FALSE, 'When "javascript_always_use_jquery" is FALSE: The JavaScript returned by drupal_get_js() when a custom JavaScript file that does not require jQuery has been added does not include the basePath Drupal setting.');
    $this->assertTrue(strpos($javascript, 'misc/collapse.js') !== FALSE, 'When "javascript_always_use_jquery" is FALSE: The JavaScript returned by drupal_get_js() when a custom JavaScript file that does not require jQuery has been added includes the custom file.');
    variable_del('javascript_always_use_jquery');

    // When 'javascript_always_use_jquery' is set to FALSE and a file that does
    // not require jQuery is added, followed by one that does, drupal_get_js()
    // should return jQuery and other standard scripts and settings, in
    // addition to both of the requested files.
    $this->resetStaticVariables();
    variable_set('javascript_always_use_jquery', FALSE);
    drupal_add_js('misc/collapse.js', array('requires_jquery' => FALSE));
    drupal_add_js('misc/ajax.js');
    $javascript = drupal_get_js();
    $this->assertTrue(strpos($javascript, 'misc/jquery.js') !== FALSE, 'When "javascript_always_use_jquery" is FALSE: The JavaScript returned by drupal_get_js() when at least one custom JavaScript file that requires jQuery has been added includes jquery.js.');
    $this->assertTrue(strpos($javascript, 'misc/drupal.js') !== FALSE, 'When "javascript_always_use_jquery" is FALSE: The JavaScript returned by drupal_get_js() when at least one custom JavaScript file that requires jQuery has been added includes drupal.js.');
    $this->assertTrue(strpos($javascript, 'Drupal.settings') !== FALSE, 'When "javascript_always_use_jquery" is FALSE: The JavaScript returned by drupal_get_js() when at least one custom JavaScript file that requires jQuery has been added includes Drupal.settings.');
    $this->assertTrue(strpos($javascript, 'basePath') !== FALSE, 'When "javascript_always_use_jquery" is FALSE: The JavaScript returned by drupal_get_js() when at least one custom JavaScript file that requires jQuery has been added includes the basePath Drupal setting.');
    $this->assertTrue(strpos($javascript, 'misc/collapse.js') !== FALSE, 'When "javascript_always_use_jquery" is FALSE: The JavaScript returned by drupal_get_js() when at least one custom JavaScript file that requires jQuery has been added includes the first custom file.');
    $this->assertTrue(strpos($javascript, 'misc/ajax.js') !== FALSE, 'When "javascript_always_use_jquery" is FALSE: The JavaScript returned by drupal_get_js() when at least one custom JavaScript file that requires jQuery has been added includes the second custom file.');
    variable_del('javascript_always_use_jquery');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
