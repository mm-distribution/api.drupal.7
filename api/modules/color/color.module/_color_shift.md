# _color_shift()

- **Type:** Function
- **File:** [`modules/color/color.module`](_file.md), lines 664–709 · [local source](../../../../source/modules/color/color.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/color/color.module#L664-L709)
- **Module/theme:** color

## Signature

```php
function _color_shift($given, $ref1, $ref2, $target)
```

## Documentation

```text
Shifts a given color, using a reference pair and a target blend color.

Note: this function is significantly different from the JS version, as it
is written to match the blended images perfectly.

Constraint: if (ref2 == target + (ref1 - target) * delta) for some fraction
delta then (return == target + (given - target) * delta).

Loose constraint: Preserve relative positions in saturation and luminance
space.
```

## Code

```php
function _color_shift($given, $ref1, $ref2, $target) {
  // We assume that ref2 is a blend of ref1 and target and find
  // delta based on the length of the difference vectors.

  // delta = 1 - |ref2 - ref1| / |white - ref1|
  $target = _color_unpack($target, TRUE);
  $ref1 = _color_unpack($ref1, TRUE);
  $ref2 = _color_unpack($ref2, TRUE);
  $numerator = 0;
  $denominator = 0;
  for ($i = 0; $i < 3; ++$i) {
    $numerator += ($ref2[$i] - $ref1[$i]) * ($ref2[$i] - $ref1[$i]);
    $denominator += ($target[$i] - $ref1[$i]) * ($target[$i] - $ref1[$i]);
  }
  $delta = ($denominator > 0) ? (1 - sqrt($numerator / $denominator)) : 0;

  // Calculate the color that ref2 would be if the assumption was true.
  for ($i = 0; $i < 3; ++$i) {
    $ref3[$i] = $target[$i] + ($ref1[$i] - $target[$i]) * $delta;
  }

  // If the assumption is not true, there is a difference between ref2 and ref3.
  // We measure this in HSL space. Notation: x' = hsl(x).
  $ref2 = _color_rgb2hsl($ref2);
  $ref3 = _color_rgb2hsl($ref3);
  for ($i = 0; $i < 3; ++$i) {
    $shift[$i] = $ref2[$i] - $ref3[$i];
  }

  // Take the given color, and blend it towards the target.
  $given = _color_unpack($given, TRUE);
  for ($i = 0; $i < 3; ++$i) {
    $result[$i] = $target[$i] + ($given[$i] - $target[$i]) * $delta;
  }

  // Finally, we apply the extra shift in HSL space.
  // Note: if ref2 is a pure blend of ref1 and target, then |shift| = 0.
  $result = _color_rgb2hsl($result);
  for ($i = 0; $i < 3; ++$i) {
    $result[$i] = min(1, max(0, $result[$i] + $shift[$i]));
  }
  $result = _color_hsl2rgb($result);

  // Return hex color.
  return _color_pack($result, TRUE);
}
```

---
_Drupal 7.103 · [modules/color/color.module](https://github.com/drupal/drupal/blob/7.103/modules/color/color.module) · Licensed GPL-2.0-or-later (see LICENSE)._
