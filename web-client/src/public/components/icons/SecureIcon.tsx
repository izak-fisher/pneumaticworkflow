/* eslint-disable */
/* prettier-ignore */
import * as React from 'react';

export type TSecureIconProps = React.SVGAttributes<SVGElement>;

export function SecureIcon({ fill = 'currentColor', ...props }: TSecureIconProps) {
  return (
    <svg width="12" height="14" viewBox="0 0 12 14" fill={fill} xmlns="http://www.w3.org/2000/svg" {...props}>
      <path fillRule="evenodd" clipRule="evenodd" d="M9.33268 4.77776H9.99935C10.7327 4.77776 11.3327 5.34919 11.3327 6.0476V12.3968C11.3327 13.0952 10.7327 13.6666 9.99935 13.6666H1.99935C1.26602 13.6666 0.666016 13.0952 0.666016 12.3968V6.0476C0.666016 5.34919 1.26602 4.77776 1.99935 4.77776H2.66602V3.50792C2.66602 1.75554 4.15935 0.333313 5.99935 0.333313C7.83935 0.333313 9.33268 1.75554 9.33268 3.50792V4.77776ZM5.99935 1.60315C4.89268 1.60315 3.99935 2.45395 3.99935 3.50792V4.77776H7.99935V3.50792C7.99935 2.45395 7.10602 1.60315 5.99935 1.60315ZM1.99935 12.3968V6.0476H9.99935V12.3968H1.99935ZM7.33268 9.2222C7.33268 9.92062 6.73268 10.492 5.99935 10.492C5.26602 10.492 4.66602 9.92062 4.66602 9.2222C4.66602 8.52379 5.26602 7.95236 5.99935 7.95236C6.73268 7.95236 7.33268 8.52379 7.33268 9.2222Z" />
    </svg>
  );
}
