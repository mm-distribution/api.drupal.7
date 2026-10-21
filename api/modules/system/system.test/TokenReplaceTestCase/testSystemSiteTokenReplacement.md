# TokenReplaceTestCase::testSystemSiteTokenReplacement()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 2300–2336 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L2300-L2336)
- **Class:** [TokenReplaceTestCase](../TokenReplaceTestCase.md)
- **Module/theme:** system

## Signature

```php
function testSystemSiteTokenReplacement()
```

## Documentation

```text
Tests the generation of all system site information tokens.
```

## Code

```php
  function testSystemSiteTokenReplacement() {
    global $language;
    $url_options = array(
      'absolute' => TRUE,
      'language' => $language,
    );

    // Set a few site variables.
    variable_set('site_name', '<strong>Drupal<strong>');
    variable_set('site_slogan', '<blink>Slogan</blink>');

    // Generate and test sanitized tokens.
    $tests = array();
    $tests['[site:name]'] = check_plain(variable_get('site_name', 'Drupal'));
    $tests['[site:slogan]'] = check_plain(variable_get('site_slogan', ''));
    $tests['[site:mail]'] = 'simpletest@example.com';
    $tests['[site:url]'] = url('<front>', $url_options);
    $tests['[site:url-brief]'] = preg_replace(array('!^https?://!', '!/$!'), '', url('<front>', $url_options));
    $tests['[site:login-url]'] = url('user', $url_options);

    // Test to make sure that we generated something for each token.
    $this->assertFalse(in_array(0, array_map('strlen', $tests)), 'No empty tokens generated.');

    foreach ($tests as $input => $expected) {
      $output = token_replace($input, array(), array('language' => $language));
      $this->assertEqual($output, $expected, format_string('Sanitized system site information token %token replaced.', array('%token' => $input)));
    }

    // Generate and test unsanitized tokens.
    $tests['[site:name]'] = variable_get('site_name', 'Drupal');
    $tests['[site:slogan]'] = variable_get('site_slogan', '');

    foreach ($tests as $input => $expected) {
      $output = token_replace($input, array(), array('language' => $language, 'sanitize' => FALSE));
      $this->assertEqual($output, $expected, format_string('Unsanitized system site information token %token replaced.', array('%token' => $input)));
    }
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
