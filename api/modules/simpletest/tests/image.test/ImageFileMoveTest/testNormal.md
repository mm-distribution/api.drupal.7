# ImageFileMoveTest::testNormal()

- **Type:** Method
- **File:** [`modules/simpletest/tests/image.test`](../_file.md), lines 556–578 · [local source](../../../../../../source/modules/simpletest/tests/image.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/image.test#L556-L578)
- **Class:** [ImageFileMoveTest](../ImageFileMoveTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testNormal()
```

## Documentation

```text
Tests moving a randomly generated image.
```

## Code

```php
  function testNormal() {
    // Pick a file for testing.
    $file = current($this->drupalGetTestFiles('image'));

    // Create derivative image.
    $style = image_style_load(key(image_styles()));
    $derivative_uri = image_style_path($style['name'], $file->uri);
    image_style_create_derivative($style, $file->uri, $derivative_uri);

    // Check if derivative image exists.
    $this->assertTrue(file_exists($derivative_uri), 'Make sure derivative image is generated successfully.');

    // Clone the object so we don't have to worry about the function changing
    // our reference copy.
    $desired_filepath = 'public://' . $this->randomName();
    $result = file_move(clone $file, $desired_filepath, FILE_EXISTS_ERROR);

    // Check if image has been moved.
    $this->assertTrue(file_exists($result->uri), 'Make sure image is moved successfully.');

    // Check if derivative image has been flushed.
    $this->assertFalse(file_exists($derivative_uri), 'Make sure derivative image has been flushed.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/image.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/image.test) · Licensed GPL-2.0-or-later (see LICENSE)._
