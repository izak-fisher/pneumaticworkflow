/* eslint-disable */
/* prettier-ignore */
import * as React from 'react';

export type TEyeIconProps = React.SVGAttributes<SVGElement>;

export const EyeIcon = ({ fill = '#010101', ...rest }: TEyeIconProps) => (
  <svg width="22" height="20" viewBox="0 0 22 20" fill={fill} xmlns="http://www.w3.org/2000/svg" {...rest}>
    <path fillRule="evenodd" clipRule="evenodd" d="M3.69 4.28198L1.01 1.48303L2.42 0L20.15 18.5274L18.74 20L15.32 16.4282C13.98 16.9817 12.52 17.2846 11 17.2846C6 17.2846 1.73 14.0366 0 9.4517C0.77 7.39426 2.06 5.6188 3.69 4.28198ZM11 3.70757C14.79 3.70757 18.17 5.93212 19.82 9.4517C19.23 10.7258 18.4 11.8225 17.41 12.7102L18.82 14.1828C20.21 12.8982 21.31 11.2898 22 9.4517C20.27 4.86684 16 1.6188 11 1.6188C9.73 1.6188 8.51 1.82768 7.36 2.2141L9.01 3.93734C9.66 3.80157 10.32 3.70757 11 3.70757ZM9.93 4.89817L12 7.06005C12.57 7.32115 13.03 7.80157 13.28 8.39687L15.35 10.5587C15.43 10.2037 15.49 9.82768 15.49 9.44125C15.5 6.85117 13.48 4.75196 11 4.75196C10.63 4.75196 10.28 4.80418 9.93 4.89817ZM8.51 9.31593L11.12 12.0418C11.08 12.0522 11.04 12.0627 11 12.0627C9.62 12.0627 8.5 10.893 8.5 9.4517C8.5 9.42559 8.5025 9.40471 8.505 9.38383C8.5075 9.36295 8.51 9.34203 8.51 9.31593ZM6.86 7.59269L5.11 5.76501C3.9 6.72585 2.88 7.95822 2.18 9.4517C3.83 12.9713 7.21 15.1958 11 15.1958C11.95 15.1958 12.87 15.0496 13.75 14.799L12.77 13.7755C12.23 14.0157 11.63 14.1514 11 14.1514C8.52 14.1514 6.5 12.0418 6.5 9.4517C6.5 8.79373 6.63 8.1671 6.86 7.59269Z" fill={fill} />
  </svg>
);