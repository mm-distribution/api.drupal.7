# ImageToolkitGdTestCase::testManipulations()

- **Type:** Method
- **File:** [`modules/simpletest/tests/image.test`](../_file.md), lines 264–511 · [local source](../../../../../../source/modules/simpletest/tests/image.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/image.test#L264-L511)
- **Class:** [ImageToolkitGdTestCase](../ImageToolkitGdTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testManipulations()
```

## Documentation

```text
Since PHP can't visually check that our images have been manipulated
properly, build a list of expected color values for each of the corners and
the expected height and widths for the final images.
```

## Code

```php
  function testManipulations() {
    // If GD isn't available don't bother testing this.
    module_load_include('inc', 'system', 'image.gd');
    if (!function_exists('image_gd_check_settings') || !image_gd_check_settings()) {
      $this->pass(t('Image manipulations for the GD toolkit were skipped because the GD toolkit is not available.'));
      return;
    }

    // Typically the corner colors will be unchanged. These colors are in the
    // order of top-left, top-right, bottom-right, bottom-left.
    $default_corners = array($this->red, $this->green, $this->blue, $this->transparent);

    // A list of files that will be tested.
    $files = array(
      'image-test.png',
      'image-test.gif',
      'image-test-no-transparency.gif',
      'image-test.jpg',
    );

    // Setup a list of tests to perform on each type.
    $operations = array(
      'resize' => array(
        'function' => 'resize',
        'arguments' => array(20, 10),
        'width' => 20,
        'height' => 10,
        'corners' => $default_corners,
      ),
      'scale_x' => array(
        'function' => 'scale',
        'arguments' => array(20, NULL),
        'width' => 20,
        'height' => 10,
        'corners' => $default_corners,
      ),
      'scale_y' => array(
        'function' => 'scale',
        'arguments' => array(NULL, 10),
        'width' => 20,
        'height' => 10,
        'corners' => $default_corners,
      ),
      'upscale_x' => array(
        'function' => 'scale',
        'arguments' => array(80, NULL, TRUE),
        'width' => 80,
        'height' => 40,
        'corners' => $default_corners,
      ),
      'upscale_y' => array(
        'function' => 'scale',
        'arguments' => array(NULL, 40, TRUE),
        'width' => 80,
        'height' => 40,
        'corners' => $default_corners,
      ),
      'crop' => array(
        'function' => 'crop',
        'arguments' => array(12, 4, 16, 12),
        'width' => 16,
        'height' => 12,
        'corners' => array_fill(0, 4, $this->white),
      ),
      'scale_and_crop' => array(
        'function' => 'scale_and_crop',
        'arguments' => array(10, 8),
        'width' => 10,
        'height' => 8,
        'corners' => array_fill(0, 4, $this->black),
      ),
    );

    // Systems using non-bundled GD2 don't have imagerotate. Test if available.
    // @todo Remove the version check once https://www.drupal.org/node/2918570
    //   is resolved.
    if (function_exists('imagerotate') && (version_compare(PHP_VERSION, '7.0.26', '<') || (version_compare(PHP_VERSION, '7.1', '>=') && version_compare(PHP_VERSION, '7.1.12', '<')))) {
      $operations += array(
        'rotate_90' => array(
          'function' => 'rotate',
          'arguments' => array(90, 0xFF00FF), // Fuchsia background.
          'width' => 20,
          'height' => 40,
          'corners' => array($this->fuchsia, $this->red, $this->green, $this->blue),
        ),
        'rotate_transparent_90' => array(
          'function' => 'rotate',
          'arguments' => array(90),
          'width' => 20,
          'height' => 40,
          'corners' => array($this->transparent, $this->red, $this->green, $this->blue),
        ),
      );
      // As of PHP version 5.5, GD uses a different algorithm to rotate images
      // than version 5.4 and below, resulting in different dimensions.
      // See https://bugs.php.net/bug.php?id=65148.
      // For the 40x20 test images, the dimensions resulting from rotation will
      // be 1 pixel smaller in both width and height in PHP 5.5 and above.
      // @todo: The PHP bug was fixed in PHP 7.0.26 and 7.1.12. Change the code
      //   below to reflect that in https://www.drupal.org/node/2918570.
      if (version_compare(PHP_VERSION, '5.5', '>=')) {
        $operations += array(
          'rotate_5' => array(
            'function' => 'rotate',
            'arguments' => array(5, 0xFF00FF), // Fuchsia background.
            'width' => 41,
            'height' => 23,
            'corners' => array_fill(0, 4, $this->fuchsia),
          ),
          'rotate_transparent_5' => array(
            'function' => 'rotate',
            'arguments' => array(5),
            'width' => 41,
            'height' => 23,
            'corners' => array_fill(0, 4, $this->rotate_transparent),
          ),
        );
      }
      else {
        $operations += array(
          'rotate_5' => array(
            'function' => 'rotate',
            'arguments' => array(5, 0xFF00FF), // Fuchsia background.
            'width' => 42,
            'height' => 24,
            'corners' => array_fill(0, 4, $this->fuchsia),
          ),
          'rotate_transparent_5' => array(
            'function' => 'rotate',
            'arguments' => array(5),
            'width' => 42,
            'height' => 24,
            'corners' => array_fill(0, 4, $this->rotate_transparent),
          ),
        );
      }
    }

    // Systems using non-bundled GD2 don't have imagefilter. Test if available.
    if (function_exists('imagefilter')) {
      $operations += array(
        'desaturate' => array(
          'function' => 'desaturate',
          'arguments' => array(),
          'height' => 20,
          'width' => 40,
          // Grayscale corners are a bit funky. Each of the corners are a shade of
          // gray. The values of these were determined simply by looking at the
          // final image to see what desaturated colors end up being.
          'corners' => array(
            array_fill(0, 3, 76) + array(3 => 0),
            array_fill(0, 3, 149) + array(3 => 0),
            array_fill(0, 3, 29) + array(3 => 0),
            array_fill(0, 3, 225) + array(3 => 127)
          ),
        ),
      );
    }

    foreach ($files as $file) {
      foreach ($operations as $op => $values) {
        // Load up a fresh image.
        $image = image_load(drupal_get_path('module', 'simpletest') . '/files/' . $file, 'gd');
        if (!$image) {
          $this->fail(t('Could not load image %file.', array('%file' => $file)));
          continue 2;
        }

        // All images should be converted to truecolor when loaded.
        $image_truecolor = imageistruecolor($image->resource);
        $this->assertTrue($image_truecolor, format_string('Image %file after load is a truecolor image.', array('%file' => $file)));

        if ($image->info['extension'] == 'gif') {
          if ($op == 'desaturate') {
            // Transparent GIFs and the imagefilter function don't work together.
            $values['corners'][3][3] = 0;
          }
        }

        // Perform our operation.
        $function = 'image_' . $values['function'];
        $arguments = array();
        $arguments[] = &$image;
        $arguments = array_merge($arguments, $values['arguments']);
        call_user_func_array($function, $arguments);

        // To keep from flooding the test with assert values, make a general
        // value for whether each group of values fail.
        $correct_dimensions_real = TRUE;
        $correct_dimensions_object = TRUE;
        $correct_colors = TRUE;

        // Check the real dimensions of the image first.
        if (imagesy($image->resource) != $values['height'] || imagesx($image->resource) != $values['width']) {
          $correct_dimensions_real = FALSE;
        }

        // Check that the image object has an accurate record of the dimensions.
        if ($image->info['width'] != $values['width'] || $image->info['height'] != $values['height']) {
          $correct_dimensions_object = FALSE;
        }
        // Now check each of the corners to ensure color correctness.
        foreach ($values['corners'] as $key => $corner) {
          // The test gif that does not have transparency has yellow where the
          // others have transparent.
          if ($file === 'image-test-no-transparency.gif' && $corner === $this->transparent) {
            $corner = $this->yellow;
          }
          // Get the location of the corner.
          switch ($key) {
            case 0:
              $x = 0;
              $y = 0;
              break;
            case 1:
              $x = $values['width'] - 1;
              $y = 0;
              break;
            case 2:
              $x = $values['width'] - 1;
              $y = $values['height'] - 1;
              break;
            case 3:
              $x = 0;
              $y = $values['height'] - 1;
              break;
          }
          $color = $this->getPixelColor($image, $x, $y);
          $correct_colors = $this->colorsAreEqual($color, $corner);
        }

        $directory = file_default_scheme() . '://imagetests';
        file_prepare_directory($directory, FILE_CREATE_DIRECTORY);
        $file_path = $directory . '/' . $op . '.' . $image->info['extension'];
        image_save($image, $file_path);

        $this->assertTrue($correct_dimensions_real, format_string('Image %file after %action action has proper dimensions.', array('%file' => $file, '%action' => $op)));
        $this->assertTrue($correct_dimensions_object, format_string('Image %file object after %action action is reporting the proper height and width values.', array('%file' => $file, '%action' => $op)));
        // JPEG colors will always be messed up due to compression.
        if ($image->info['extension'] != 'jpg') {
          $this->assertTrue($correct_colors, format_string('Image %file object after %action action has the correct color placement.', array('%file' => $file, '%action' => $op)));
        }
      }

      // Check that saved image reloads without raising PHP errors.
      $image_reloaded = image_load($file_path);
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/image.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/image.test) · Licensed GPL-2.0-or-later (see LICENSE)._
