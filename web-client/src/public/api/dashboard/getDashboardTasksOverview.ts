import { commonRequest } from '../commonRequest';
import { getBrowserConfigEnv } from '../../utils/getConfig';
import { TDashboardTimeRangeDates } from '../../types/dashboard';

export interface IGetDashboardOverviewResponse {
  completed: number;
  inProgress: number;
  overdue: number;
  started: number;
}

export function getDashboardTasksOverview(params: TDashboardTimeRangeDates) {
  const {
    api: { urls },
  } = getBrowserConfigEnv();

  const baseUrl = urls.getDashboardTasksOverview;
  const query = getDashboardTasksOverviewQueryString(params);
  const url = `${baseUrl}${query}`;

  return commonRequest<IGetDashboardOverviewResponse>(
    url,
    {},
    {
      shouldThrow: true,
    },
  );
}

export function getDashboardTasksOverviewQueryString({ startDate, endDate, now }: TDashboardTimeRangeDates) {
  const params = [
    startDate && `date_from_tsp=${startDate.getTime() / 1000}`,
    endDate && `date_to_tsp=${endDate.getTime() / 1000}`,
    now && 'now=true',
  ]
    .filter(Boolean)
    .join('&');

  return params ? `?${params}` : '';
}